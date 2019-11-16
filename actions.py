from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet, AllSlotsReset, Restarted
import zomatopy
import json

from commonFunctions import get_soundex, send_email


class RestaurantSearch(Action):
    '''This class performs restaurant search for given location, cuisine and price parameters.
    It also prepares email text to be sent with top 10 results
    If no results are found, response is sent accordingly'''

    def name(self):
        return 'action_restaurant_search'

    def run(self, dispatcher, tracker, domain):
        #Set Zomato API key and initialize zomato
        config = {"user_key": "9afb445bef2ef4d36f34b42134a22bde"}
        zomato = zomatopy.initialize_app(config)

        #Get cuisine
        cuisines = ['chinese', 'mexican', 'italian', 'american', 'south indian', 'north indian']
        final_cuisines = []
        selected_cuisines = tracker.get_slot('cuisine')
        if selected_cuisines is None:
            final_cuisines = cuisines
        else:
            soundex_cuisines = {get_soundex(c): c for c in cuisines}
            for c in selected_cuisines:
                if get_soundex(c) in soundex_cuisines.keys():
                    final_cuisines.append(soundex_cuisines[get_soundex(c)])

        #Get price
        price = tracker.get_slot('price')

        #Get location
        loc = tracker.get_slot('location')
        if loc is None: #If location is not specified, show appropriate message
            dispatcher.utter_template("utter_default", tracker)
            return
        #Get location details from zomato
        location_detail = zomato.get_location(loc, 1)
        zomato_loc = json.loads(location_detail)
        try:
            latitude = zomato_loc["location_suggestions"][0]["latitude"]
            longitude = zomato_loc["location_suggestions"][0]["longitude"]
            cuisines_codes = {'american': 1, 'chinese': 25, 'mexican': 73, 'italian': 55, 'north indian': 50,
                              'south indian': 85}
            rest_list = []
            #Call Zomato API restaurant search
            for c in final_cuisines:
                results = zomato.restaurant_search("", latitude, longitude, str(cuisines_codes.get(c)), limit=300)
                res = json.loads(results)
                rest_list.extend(res['restaurants'])
            rest_list_formatted = []
            for restaurant in rest_list:
                rest_list_formatted.append((restaurant['restaurant']['name'],
                                            restaurant['restaurant']['location']['address'],
                                            float(restaurant['restaurant']['average_cost_for_two']),
                                            float(restaurant['restaurant']['user_rating']['aggregate_rating'])))
            rest_list_formatted = sorted(rest_list_formatted, key=lambda x: x[3], reverse=True)

            if price is None:
                #price = [0, 10000]
                dispatcher.utter_template("utter_ask_price", tracker)
                return
            if "low" in price:
                price = [0, 300]
            elif "moderate" in price:
                price = [300, 700]
            elif "high" in price:
                price = [700, 10000]
            if len(price) == 1:
                price.append(0)
            price = list(map(float, price))
            price = sorted(price)
            #Filter restaurant results based on price
            final_rest_list = list(filter(lambda x: x[2] >= price[0] and x[2] <= price[1], rest_list_formatted))[:10]

            #prepare response
            response = ""
            if len(final_rest_list) == 0:
                response = "no results"
            else:
                for restaurant in final_rest_list[:5]:
                    response = response + restaurant[0] + " in " + restaurant[1] + " has been rated " + str(
                        restaurant[3]) + "\n"

                file = open("email.txt", "w")
                file.write("Restaurant recommendations for {} food in {} are:\n".format(",".join(final_cuisines), loc))
                counter = 1
                for restaurant in final_rest_list[:10]:
                    file.write(
                        "{}. Restaurant Name: {}\n Restaurant locality Address: {}\n Average budget for two people: {}\n Zomato user rating: {}\n\n".format(
                            counter, restaurant[0], restaurant[1], restaurant[2], restaurant[3]))
                    counter += 1
                if counter<10:
                    file.write("We only found {} recommendations\n".format(str(counter-1)))
                file.close()
        except:
            response = "no results"

        dispatcher.utter_message(response)
        if response == "no results":
            dispatcher.utter_template("utter_result_not_found", tracker)
            return [SlotSet('cuisine', final_cuisines), SlotSet('location', loc), SlotSet('price', price), SlotSet('result_found', "no")]
        else:
            dispatcher.utter_template("utter_email_required", tracker)
            return [SlotSet('cuisine', final_cuisines), SlotSet('location', loc), SlotSet('price', price), SlotSet('result_found', "yes")]


class CitySearch(Action):
    '''This class performs checks on location specified.
    If city is not in tier-1 or tier-2, it shown appropriate message
    Search is performed based on soundex code'''
    def name(self):
        return 'action_get_city'

    def run(self, dispatcher, tracker, domain):
        f = open("supportedCities.txt", "r")
        cities_str = f.read()
        cities = cities_str.split(",")

        #Get soundex of all the tier-1 and tier-2 cities
        soundex_cities = {get_soundex(city): city for city in cities}

        loc = tracker.get_slot('location')
        loc_found = True
        if loc is not None:
            soundex_loc = get_soundex(loc)
            if soundex_loc in soundex_cities.keys():
                loc = soundex_cities[soundex_loc]
            else:
                dispatcher.utter_template("utter_no_service_location", tracker)
                loc_found = False
        else:
            dispatcher.utter_template("utter_no_service_location", tracker)
            loc_found = False
        return [SlotSet('location', loc), SlotSet('location_supported', "yes" if loc_found else "no")]


class SendEmail(Action):
    '''This class sends email to given email address and if something goes wrong, show appropriate message'''
    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        emails = tracker.get_slot('email')
        if emails is None:
            dispatcher.utter_template("utter_email_error", tracker)
            return
        to_email = [x.strip() for x in emails]

        emailSubject = "Restaurant recommendations for " + ",".join(
            tracker.get_slot("cuisine")) + " food in " + tracker.get_slot("location").title()
        res = send_email(to_email, emailSubject)

        if res == "success":
            dispatcher.utter_template("utter_email_sent", tracker)
        else:
            dispatcher.utter_template("utter_email_error", tracker)

        return [SlotSet('email', to_email)]


class GetCuisine(Action):
    '''This class gets the cuisine if option number is specified'''
    def name(self):
        return 'action_get_cuisine'

    def run(self, dispatcher, tracker, domain):
        cuisine_option = tracker.get_slot('option')
        if cuisine_option is None:
            dispatcher.utter_template("utter_incorrect_option", tracker)
            return
        cuisines = ['chinese', 'mexican', 'italian', 'american', 'south indian', 'north indian']
        selected_cuisines = []
        try:
            for o in cuisine_option:
                if o in ["All", "Anything"]:
                    selected_cuisines = cuisines
                    break
                elif o.lower() in cuisines:
                    selected_cuisines.append(o.lower())
                else:
                    selected_cuisines.append(cuisines[int(o) - 1])
            return [SlotSet('cuisine', selected_cuisines)]
        except:
            dispatcher.utter_template("utter_incorrect_option", tracker)


class GetPrice(Action):
    '''This class gets the price if option number is specified'''
    def name(self):
        return 'action_get_price'

    def run(self, dispatcher, tracker, domain):
        price_option = tracker.get_slot('option')
        if price_option is None:
            dispatcher.utter_template("utter_incorrect_option", tracker)
            return
        prices = [[0, 300], [300, 700], [700, 10000]]
        selected_prices = []
        try:
            for p in price_option:
                if p in ["All", "Anything"]:
                    selected_prices = prices
                    break
                else:
                    selected_prices.append(prices[int(p) - 1])
            p = [x for priceList in selected_prices for x in priceList]
            selected_prices = [min(p), max(p)]
            return [SlotSet('price', selected_prices)]
        except:
            dispatcher.utter_template("utter_incorrect_option", tracker)


class ResetAllSlots(Action):
    '''Reset all slots'''
    def name(self):
        return 'action_reset'

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]


class Restart(Action):
    '''Restart conversation and start over'''
    def name(self):
        return 'action_restarted'

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]

