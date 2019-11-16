## Generated Story -9148049444718928069
* greet
    - utter_greet
* restaurant_search{"location": "gurugram"}
    - slot{"location": "gurugram"}
    - action_get_city
    - slot{"location": "Gurugram"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "2"}
    - slot{"option": ["1", "2"]}
    - action_get_cuisine
    - slot{"cuisine": ["chinese", "mexican"]}
    - utter_ask_price
* get_option{"option": "3"}
    - slot{"option": ["3"]}
    - action_get_price
    - slot{"price": [700, 10000]}
    - action_restaurant_search
    - slot{"cuisine": ["chinese", "mexican"]}
    - slot{"location": "Gurugram"}
    - slot{"price": [700.0, 10000.0]}
    - slot{"result_found": "yes"}
* affirm
    - utter_ask_email
* send_email{"email": "surana.shilpa91@gmail.com"}
    - slot{"email": ["surana.shilpa91@gmail.com"]}
    - action_send_email
    - slot{"email": ["surana.shilpa91@gmail.com"]}
    - action_restart
    - export

## Generated Story 1842245917248005144
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "bangalore"}
    - slot{"cuisine": ["mexican"]}
    - slot{"location": "bangalore"}
    - action_get_city
    - slot{"location": "Bangalore"}
    - slot{"location_supported": "yes"}
    - utter_ask_price
* get_option{"option": "2"}
    - slot{"option": ["2"]}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant_search
    - slot{"cuisine": ["mexican"]}
    - slot{"location": "Bangalore"}
    - slot{"price": [300.0, 700.0]}
    - slot{"result_found": "yes"}
* affirm
    - utter_ask_email
* send_email{"email": "varun.tahin2210@gmail.com"}
    - slot{"email": ["varun.tahin2210@gmail.com"]}
    - action_send_email
    - slot{"email": ["varun.tahin2210@gmail.com"]}
    - action_restart
    - export


## Generated Story -624714829887831702
* greet
    - utter_greet
* restaurant_search
    - utter_default
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": ["chinese"]}
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_get_city
    - slot{"location": "Hyderabad"}
    - slot{"location_supported": "yes"}
    - utter_ask_price
* get_option{"option": "2"}
    - slot{"option": ["2"]}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant_search
    - slot{"cuisine": ["chinese"]}
    - slot{"location": "Hyderabad"}
    - slot{"price": [300.0, 700.0]}
    - slot{"result_found": "yes"}
* affirm
    - utter_ask_email
* send_email
    - utter_default
* send_email{"email": "p512uu@gmail.com"}
    - slot{"email": ["p512uu@gmail.com"]}
    - action_send_email
    - slot{"email": ["p512uu@gmail.com"]}
    - action_restart
    - export


## Generated Story 7114209112464477783
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": ["Italian"]}
    - utter_ask_location
* send_email{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_get_city
    - slot{"location": "Mumbai"}
    - slot{"location_supported": "yes"}
    - utter_ask_price
* get_option{"option": "2"}
    - slot{"option": ["2"]}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant_search
    - slot{"cuisine": ["italian"]}
    - slot{"location": "Mumbai"}
    - slot{"price": [300.0, 700.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story 4860155874834907227
* greet
    - utter_greet
* restaurant_search
    - utter_default
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": ["american"]}
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_get_city
    - slot{"location": "Hyderabad"}
    - slot{"location_supported": "yes"}
    - utter_ask_price
* get_option{"option": "2"}
    - slot{"option": ["2"]}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant_search
    - slot{"cuisine": ["american"]}
    - slot{"location": "Hyderabad"}
    - slot{"price": [300.0, 700.0]}
    - slot{"result_found": "yes"}
* affirm
    - utter_ask_email
* send_email{"email": "p512uu@gmail.com"}
    - slot{"email": ["p512uu@gmail.com"]}
    - action_send_email
    - slot{"email": ["p512uu@gmail.com"]}
    - action_restart
    - export


## Generated Story 156585155799016712
* greet
    - utter_greet
* restaurant_search{"location": "mysore"}
    - slot{"location": "mysore"}
    - action_get_city
    - slot{"location": "Mysore"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "5"}
    - slot{"option": ["5"]}
    - action_get_cuisine
    - slot{"cuisine": ["south indian"]}
    - utter_ask_price
* get_option{"option": "2"}
    - slot{"option": ["2"]}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant_search
    - slot{"cuisine": ["south indian"]}
    - slot{"location": "Mysore"}
    - slot{"price": [300.0, 700.0]}
    - slot{"result_found": "yes"}
* affirm
    - utter_ask_email
* send_email{"email": "veer.tahin@gmail.com"}
    - slot{"email": ["veer.tahin@gmail.com"]}
    - action_send_email
    - slot{"email": ["veer.tahin@gmail.com"]}
    - action_restart
    - export


## Generated Story -2883827523182892468
* restaurant_search{"cuisine": "mexican", "location": "lucknow"}
    - slot{"cuisine": ["mexican"]}
    - slot{"location": "lucknow"}
    - action_get_city
    - slot{"location": "Lucknow"}
    - slot{"location_supported": "yes"}
    - utter_ask_price
* get_option{"option": "2"}
    - slot{"option": ["2"]}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant_search
    - slot{"cuisine": ["mexican"]}
    - slot{"location": "Lucknow"}
    - slot{"price": [300.0, 700.0]}
    - slot{"result_found": "yes"}
* affirm
    - utter_ask_email
* send_email{"email": "surana.shilpa91@gmail.com"}
    - slot{"email": ["veer.tahin@gmail.com", "surana.shilpa91@gmail.com"]}
    - action_send_email
    - slot{"email": ["veer.tahin@gmail.com", "surana.shilpa91@gmail.com"]}
    - action_restart
    - export


## Generated Story -7869984315620683247
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "pune"}
    - slot{"cuisine": ["chinese"]}
    - slot{"location": "pune"}
    - action_get_city
    - slot{"location": "Pune"}
    - slot{"location_supported": "yes"}
    - utter_ask_price
* get_option{"option": "3"}
    - slot{"option": ["3"]}
    - action_get_price
    - slot{"price": [700, 10000]}
    - action_restaurant_search
    - slot{"cuisine": ["chinese"]}
    - slot{"location": "Pune"}
    - slot{"price": [700.0, 10000.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story 507388587783562950
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_get_city
    - slot{"location": "rishikesh"}
    - slot{"location_supported": "no"}
* restaurant_search{"cuisine": "chinese", "location": "kanpur"}
    - slot{"cuisine": ["chinese"]}
    - slot{"location": "kanpur"}
    - action_get_city
    - slot{"location": "Kanpur"}
    - slot{"location_supported": "yes"}
    - utter_ask_price
* get_option{"option": "3"}
    - slot{"option": ["3"]}
    - action_get_price
    - slot{"price": [700, 10000]}
    - action_restaurant_search
    - slot{"cuisine": ["chinese"]}
    - slot{"location": "Kanpur"}
    - slot{"price": [700.0, 10000.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story -812397535067193988
* restaurant_search{"cuisine": "mexican", "location": "amritsar"}
    - slot{"cuisine": ["mexican"]}
    - slot{"location": "amritsar"}
    - action_get_city
    - slot{"location": "Amritsar"}
    - slot{"location_supported": "yes"}
    - utter_ask_price
* get_option{"option": "2"}
    - slot{"option": ["2"]}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant_search
    - slot{"cuisine": ["mexican"]}
    - slot{"location": "Amritsar"}
    - slot{"price": [300.0, 700.0]}
    - slot{"result_found": "yes"}
* affirm
    - utter_ask_email
* send_email{"email": "veer.tahin@gmail.com"}
    - slot{"email": ["veer.tahin@gmail.com"]}
    - action_send_email
    - slot{"email": ["veer.tahin@gmail.com"]}
    - action_restart
    - export

## Generated Story 5574576357908107650
* restaurant_search{"cuisine": "italian", "location": "varanasi"}
    - slot{"cuisine": ["italian"]}
    - slot{"location": "varanasi"}
    - action_get_city
    - slot{"location": "Varanasi"}
    - slot{"location_supported": "yes"}
    - utter_ask_price
* get_option{"option": "3"}
    - slot{"option": ["3"]}
    - action_get_price
    - slot{"price": [700, 10000]}
    - action_restaurant_search
    - slot{"cuisine": ["italian"]}
    - slot{"location": "Varanasi"}
    - slot{"price": [700.0, 10000.0]}
    - slot{"result_found": "yes"}
* affirm
    - utter_ask_email
* send_email{"email": "veer.tahin@gmail.com"}
    - slot{"email": ["veer.tahin@gmail.com"]}
    - action_send_email
    - slot{"email": ["veer.tahin@gmail.com"]}
    - action_restart
    - export

## Generated Story 8459685758448537736
* greet
    - utter_greet
* restaurant_search{"price": "moderate"}
    - slot{"price": ["moderate"]}
    - utter_ask_location
* restaurant_search{"location": "indore"}
    - slot{"location": "indore"}
    - action_get_city
    - slot{"location": "Indore"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "2"}
    - slot{"option": ["2"]}
    - action_get_cuisine
    - slot{"cuisine": ["mexican"]}
    - action_restaurant_search
    - slot{"cuisine": ["mexican"]}
    - slot{"location": "Indore"}
    - slot{"price": [300.0, 700.0]}
    - slot{"result_found": "yes"}
* send_email
    - utter_ask_email
* send_email{"email": "p512uu@gmail.com"}
    - slot{"email": ["p512uu@gmail.com"]}
    - action_send_email
    - slot{"email": ["p512uu@gmail.com"]}
    - action_restart
    - export

## Generated Story -8964505577296916739
* greet
    - utter_greet
* restaurant_search{"price": "moderate"}
    - slot{"price": ["moderate"]}
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_get_city
    - slot{"location": "Kolkata"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "8"}
    - slot{"option": ["8"]}
    - action_get_cuisine
* get_option{"option": "4"}
    - slot{"option": ["4"]}
    - action_get_cuisine
    - slot{"cuisine": ["american"]}
    - action_restaurant_search
    - slot{"cuisine": ["american"]}
    - slot{"location": "Kolkata"}
    - slot{"price": [300.0, 700.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story -8964505577296916739
* greet
    - utter_greet
* restaurant_search{"price": "moderate"}
    - slot{"price": ["moderate"]}
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_get_city
    - slot{"location": "Kolkata"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "9"}
    - slot{"option": ["9"]}
    - action_get_cuisine
* get_option{"option": "4"}
    - slot{"option": ["4"]}
    - action_get_cuisine
    - slot{"cuisine": ["american"]}
    - action_restaurant_search
    - slot{"cuisine": ["american"]}
    - slot{"location": "Kolkata"}
    - slot{"price": [300.0, 700.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story -8964505577296916739
* greet
    - utter_greet
* restaurant_search{"price": "moderate"}
    - slot{"price": ["moderate"]}
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_get_city
    - slot{"location": "Kolkata"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "8"}
    - slot{"option": ["8"]}
    - action_get_cuisine
* get_option{"option": "9"}
    - slot{"option": ["9"]}
    - action_get_cuisine
* get_option{"option": "4"}
    - slot{"option": ["4"]}
    - action_get_cuisine
    - slot{"cuisine": ["american"]}
    - action_restaurant_search
    - slot{"cuisine": ["american"]}
    - slot{"location": "Kolkata"}
    - slot{"price": [300.0, 700.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story -8964505577296916739
* greet
    - utter_greet
* restaurant_search{"price": "moderate"}
    - slot{"price": ["moderate"]}
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_get_city
    - slot{"location": "Kolkata"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "8"}
    - slot{"option": ["8"]}
    - action_get_cuisine
* get_option{"option": "9"}
    - slot{"option": ["9"]}
    - action_get_cuisine
* get_option{"option": "4"}
    - slot{"option": ["4"]}
    - action_get_cuisine
    - slot{"cuisine": ["american"]}
    - action_restaurant_search
    - slot{"cuisine": ["american"]}
    - slot{"location": "Kolkata"}
    - slot{"price": [300.0, 700.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export


## Generated Story 1897888293185505231
* restaurant_search{"price": "600"}
    - slot{"price": ["0", "600"]}
    - utter_ask_location
* restaurant_search
    - utter_default
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_get_city
    - slot{"location": "Kolkata"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": ["mexican"]}
    - action_restaurant_search
    - slot{"cuisine": ["mexican"]}
    - slot{"location": "Kolkata"}
    - slot{"price": [0.0, 600.0]}
    - slot{"result_found": "yes"}
* send_email{"email": "p512uu@gmail.com"}
    - slot{"email": ["p512uu@gmail.com"]}
    - action_send_email
    - slot{"email": ["p512uu@gmail.com"]}
    - action_restart
    - export

## Generated Story -7566121805938374572
* restaurant_search{"price": "high"}
    - slot{"price": ["high"]}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_get_city
    - slot{"location": "Bangalore"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "2"}
    - slot{"option": ["2"]}
    - action_get_cuisine
    - slot{"cuisine": ["mexican"]}
    - action_restaurant_search
    - slot{"cuisine": ["mexican"]}
    - slot{"location": "Bangalore"}
    - slot{"price": [700.0, 10000.0]}
    - slot{"result_found": "yes"}
* send_email{"email": "p512uu@gmail.com"}
    - slot{"email": ["p512uu@gmail.com"]}
    - action_send_email
    - slot{"email": ["p512uu@gmail.com"]}
    - action_restart
    - export



## Generated Story -7491261654217886097
* greet
    - utter_greet
* restaurant_search{"price": "high", "location": "kolkata"}
    - slot{"location": "kolkata"}
    - slot{"price": ["high"]}
    - action_get_city
    - slot{"location": "Kolkata"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "2"}
    - slot{"option": ["2"]}
    - action_get_cuisine
    - slot{"cuisine": ["mexican"]}
    - action_restaurant_search
    - slot{"cuisine": ["mexican"]}
    - slot{"location": "Kolkata"}
    - slot{"price": [700.0, 10000.0]}
    - slot{"result_found": "yes"}
* affirm
    - utter_ask_email
* send_email{"email": "p512uu@gmail.com"}
    - slot{"email": ["p512uu@gmail.com"]}
    - action_send_email
    - slot{"email": ["p512uu@gmail.com"]}
    - action_restart
    - export


## Generated Story 2156496590186950352
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": ["chinese"]}
    - slot{"location": "chandigarh"}
    - action_get_city
    - slot{"location": "Chandigarh"}
    - slot{"location_supported": "yes"}
    - utter_ask_price
* get_option{"option": "3"}
    - slot{"option": ["3"]}
    - action_get_price
    - slot{"price": [700, 10000]}
    - action_restaurant_search
    - slot{"cuisine": ["chinese"]}
    - slot{"location": "Chandigarh"}
    - slot{"price": [700.0, 10000.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story -8154541334482862957
* greet
    - utter_greet
* restaurant_search{"location": "bangalore", "price": "500"}
    - slot{"location": "bangalore"}
    - slot{"price": ["10000", "500"]}
    - action_get_city
    - slot{"location": "Bangalore"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "6"}
    - slot{"option": ["6"]}
    - action_get_cuisine
    - slot{"cuisine": ["north indian"]}
    - action_restaurant_search
    - slot{"cuisine": ["north indian"]}
    - slot{"location": "Bangalore"}
    - slot{"price": [500.0, 10000.0]}
    - slot{"result_found": "yes"}
* affirm
    - utter_ask_email
* send_email{"email": "veer.tahin@gmail.com"}
    - slot{"email": ["veer.tahin@gmail.com"]}
    - action_send_email
    - slot{"email": ["veer.tahin@gmail.com"]}
    - action_restart
    - export

## Generated Story 1158455781907593013
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "price": "1000"}
    - slot{"cuisine": ["american"]}
    - slot{"price": ["500", "1000"]}
    - utter_ask_location
* restaurant_search{"location": "jabalpur"}
    - slot{"location": "jabalpur"}
    - action_get_city
    - slot{"location": "Jabalpur"}
    - slot{"location_supported": "yes"}
    - action_restaurant_search
    - slot{"cuisine": ["american"]}
    - slot{"location": "Jabalpur"}
    - slot{"price": [500.0, 1000.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story 7701017157626719240
* goodbye
    - utter_goodbye
    - action_restart
    - export

## Generated Story -4182666464912573307
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* goodbye
    - utter_goodbye
    - action_restart
    - export

## Generated Story -4182666464912573308
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story 1919275962849152006
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price": "500"}
    - slot{"location": "delhi"}
    - slot{"price": ["300", "500"]}
    - action_get_city
    - slot{"location": "Delhi"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "3"}
    - slot{"option": ["3"]}
    - action_get_cuisine
    - slot{"cuisine": ["italian"]}
    - action_restaurant_search
    - slot{"cuisine": ["italian"]}
    - slot{"location": "Delhi"}
    - slot{"price": [300.0, 500.0]}
    - slot{"result_found": "yes"}
* send_email{"email": "p512uu@gmail.com"}
    - slot{"email": ["p512uu@gmail.com"]}
    - action_send_email
    - slot{"email": ["p512uu@gmail.com"]}
    - action_restart
    - export

## Generated Story -2661818604032223760
* greet
    - utter_greet
* goodbye
    - utter_goodbye
    - action_restart
    - export

## Generated Story -653057028365245522
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_get_city
    - slot{"location": "Kolkata"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "1"}
    - slot{"option": ["1"]}
    - action_get_cuisine
    - slot{"cuisine": ["chinese"]}
    - utter_ask_price
* get_option{"option": "1"}
    - slot{"option": ["1"]}
    - action_get_price
    - slot{"price": [0, 300]}
    - action_restaurant_search
    - slot{"cuisine": ["chinese"]}
    - slot{"location": "Kolkata"}
    - slot{"price": [0.0, 300.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story -7337081067371179755
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_get_city
    - slot{"location": "Chennai"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "2"}
    - slot{"option": ["2"]}
    - action_get_cuisine
    - slot{"cuisine": ["mexican"]}
    - utter_ask_price
* get_option{"option": "2"}
    - slot{"option": ["2"]}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant_search
    - slot{"cuisine": ["mexican"]}
    - slot{"location": "Chennai"}
    - slot{"price": [300.0, 700.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story -6539057534157085023
* restaurant_search{"location": "mysore"}
    - slot{"location": "mysore"}
    - action_get_city
    - slot{"location": "Mysore"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "3"}
    - slot{"option": ["3"]}
    - action_get_cuisine
    - slot{"cuisine": ["italian"]}
    - utter_ask_price
* get_option{"option": "2"}
    - slot{"option": ["2"]}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant_search
    - slot{"cuisine": ["italian"]}
    - slot{"location": "Mysore"}
    - slot{"price": [300.0, 700.0]}
    - slot{"result_found": "yes"}
* get_option
    - utter_goodbye
    - action_restart
    - export

## Generated Story -5984225514500218276
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - action_get_city
    - slot{"location": "Ahmedabad"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "4"}
    - slot{"option": ["4"]}
    - action_get_cuisine
    - slot{"cuisine": ["american"]}
    - utter_ask_price
* get_option{"option": "3"}
    - slot{"option": ["3"]}
    - action_get_price
    - slot{"price": [700, 10000]}
    - action_restaurant_search
    - slot{"cuisine": ["american"]}
    - slot{"location": "Ahmedabad"}
    - slot{"price": [700.0, 10000.0]}
    - slot{"result_found": "yes"}
* affirm
    - utter_ask_email
* send_email{"email": "veer.tahin@gmail.com"}
    - slot{"email": ["veer.tahin@gmail.com"]}
    - action_send_email
    - slot{"email": ["veer.tahin@gmail.com"]}
    - action_restart
    - export

## Generated Story 2564624548093252291
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_get_city
    - slot{"location": "Hyderabad"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "6"}
    - slot{"option": ["6"]}
    - action_get_cuisine
    - slot{"cuisine": ["north indian"]}
    - utter_ask_price
* get_option{"option": "3"}
    - slot{"option": ["3"]}
    - action_get_price
    - slot{"price": [700, 10000]}
    - action_restaurant_search
    - slot{"cuisine": ["north indian"]}
    - slot{"location": "Hyderabad"}
    - slot{"price": [700.0, 10000.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story 5560202022623095868
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_get_city
    - slot{"location": "Pune"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "5"}
    - slot{"option": ["5"]}
    - action_get_cuisine
    - slot{"cuisine": ["south indian"]}
    - utter_ask_price
* get_option{"option": "2"}
    - slot{"option": ["2"]}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant_search
    - slot{"cuisine": ["south indian"]}
    - slot{"location": "Pune"}
    - slot{"price": [300.0, 700.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story -3583801775102666064
* greet
    - utter_greet
* restaurant_search{"location": "kota"}
    - slot{"location": "kota"}
    - action_get_city
    - slot{"location": "Kota"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "1"}
    - slot{"option": ["1"]}
    - action_get_cuisine
    - slot{"cuisine": ["chinese"]}
    - utter_ask_price
* get_option{"option": "1"}
    - slot{"option": ["1"]}
    - action_get_price
    - slot{"price": [0, 300]}
    - action_restaurant_search
    - slot{"cuisine": ["chinese"]}
    - slot{"location": "Kota"}
    - slot{"price": [0.0, 300.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story 3951243220982397947
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_get_city
    - slot{"location": "Mumbai"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "2"}
    - slot{"option": ["2"]}
    - action_get_cuisine
    - slot{"cuisine": ["mexican"]}
    - utter_ask_price
* get_option{"option": "2"}
    - slot{"option": ["2"]}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant_search
    - slot{"cuisine": ["mexican"]}
    - slot{"location": "Mumbai"}
    - slot{"price": [300.0, 700.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story -1670390917347108379
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ajmer"}
    - slot{"location": "ajmer"}
    - action_get_city
    - slot{"location": "Ajmer"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "6"}
    - slot{"option": ["6"]}
    - action_get_cuisine
    - slot{"cuisine": ["north indian"]}
    - utter_ask_price
* get_option{"option": "1"}
    - slot{"option": ["1"]}
    - action_get_price
    - slot{"price": [0, 300]}
    - action_restaurant_search
    - slot{"cuisine": ["north indian"]}
    - slot{"location": "Ajmer"}
    - slot{"price": [0.0, 300.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story 5577614056324457248
* greet
    - utter_greet
* restaurant_search{"price": "high", "location": "bhopal"}
    - slot{"location": "bhopal"}
    - slot{"price": ["high"]}
    - action_get_city
    - slot{"location": "Bhopal"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "2"}
    - slot{"option": ["2"]}
    - action_get_cuisine
    - slot{"cuisine": ["mexican"]}
    - action_restaurant_search
    - slot{"cuisine": ["mexican"]}
    - slot{"location": "Bhopal"}
    - slot{"price": [700.0, 10000.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story 5461889637716585362
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_get_city
    - slot{"location": "Delhi"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "3"}
    - slot{"option": ["3"]}
    - action_get_cuisine
    - slot{"cuisine": ["italian"]}
    - utter_ask_price
* get_option{"option": "2"}
    - slot{"option": ["2"]}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant_search
    - slot{"cuisine": ["italian"]}
    - slot{"location": "Delhi"}
    - slot{"price": [300.0, 700.0]}
    - slot{"result_found": "yes"}
* affirm
    - utter_ask_email
* send_email{"email": "veer.tahin@gmail.com"}
    - slot{"email": ["veer.tahin@gmail.com"]}
    - action_send_email
    - slot{"email": ["veer.tahin@gmail.com"]}
    - action_restart
    - export

## Generated Story -3321749545263128009
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_get_city
    - slot{"location": "Bangalore"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": ["south indian"]}
    - utter_ask_price
* restaurant_search{"price": "700"}
    - slot{"price": ["300", "700"]}
    - action_restaurant_search
    - slot{"cuisine": ["south indian"]}
    - slot{"location": "Bangalore"}
    - slot{"price": [300.0, 700.0]}
    - slot{"result_found": "yes"}
* affirm
    - utter_ask_email
* send_email{"email": "veer.tahin@gmail.com"}
    - slot{"email": ["veer.tahin@gmail.com"]}
    - action_send_email
    - slot{"email": ["veer.tahin@gmail.com"]}
    - action_restart
    - export



## Generated Story -1302896034567610055
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_get_city
    - slot{"location": "rishikesh"}
    - slot{"location_supported": "no"}
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_get_city
    - slot{"location": "Pune"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "2"}
    - slot{"option": ["2"]}
    - action_get_cuisine
    - slot{"cuisine": ["mexican"]}
    - utter_ask_price
* get_option{"option": "3"}
    - slot{"option": ["3"]}
    - action_get_price
    - slot{"price": [700, 10000]}
    - action_restaurant_search
    - slot{"cuisine": ["mexican"]}
    - slot{"location": "Pune"}
    - slot{"price": [700.0, 10000.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story 4010194580654260906
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_get_city
    - slot{"location": "Kolkata"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": ["american"]}
    - utter_ask_price
* restaurant_search{"price": "300"}
    - slot{"price": ["0", "300"]}
    - action_restaurant_search
    - slot{"cuisine": ["american"]}
    - slot{"location": "Kolkata"}
    - slot{"price": [0.0, 300.0]}
    - slot{"result_found": "yes"}
* affirm
    - utter_ask_email
* send_email{"email": "veer.tahin@gmail.com"}
    - slot{"email": ["veer.tahin@gmail.com"]}
    - action_send_email
    - slot{"email": ["veer.tahin@gmail.com"]}
    - action_restart
    - export

## Generated Story 497663144875166255
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": ["chinese"]}
    - slot{"location": "chandigarh"}
    - action_get_city
    - slot{"location": "Chandigarh"}
    - slot{"location_supported": "yes"}
    - utter_ask_price
* restaurant_search{"price": "300"}
    - slot{"price": ["0", "300"]}
    - action_restaurant_search
    - slot{"cuisine": ["chinese"]}
    - slot{"location": "Chandigarh"}
    - slot{"price": [0.0, 300.0]}
    - slot{"result_found": "yes"}
* affirm
    - utter_ask_email
* send_email{"email": "veer.tahin@gmail.com"}
    - slot{"email": ["veer.tahin@gmail.com"]}
    - action_send_email
    - slot{"email": ["veer.tahin@gmail.com"]}
    - action_restart
    - export

## Generated Story -448019550900761936
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_get_city
    - slot{"location": "mubaim"}
    - slot{"location_supported": "no"}
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_get_city
    - slot{"location": "Mumbai"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": ["italian"]}
    - utter_ask_price
* restaurant_search{"price": "300"}
    - slot{"price": ["0", "300"]}
    - action_restaurant_search
    - slot{"cuisine": ["italian"]}
    - slot{"location": "Mumbai"}
    - slot{"price": [0.0, 300.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story 1900156611422370700
* greet
    - utter_greet
* restaurant_search{"location": "kanchi"}
    - slot{"location": "kanchi"}
    - action_get_city
    - slot{"location": "kanchi"}
    - slot{"location_supported": "no"}
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_get_city
    - slot{"location": "Kolkata"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": ["north indian"]}
    - utter_ask_price
* restaurant_search{"price": "300"}
    - slot{"price": ["10000", "300"]}
    - action_restaurant_search
    - slot{"cuisine": ["north indian"]}
    - slot{"location": "Kolkata"}
    - slot{"price": [300.0, 10000.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story -4801069463492850792
* greet
    - utter_greet
* restaurant_search{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - action_get_city
    - slot{"location": "Kanpur"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* restaurant_search
    - action_get_cuisine
* restaurant_search
    - action_get_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": ["mexican"]}
    - utter_ask_price
* restaurant_search{"price": "500"}
    - slot{"price": ["300", "500"]}
    - action_restaurant_search
    - slot{"cuisine": ["mexican"]}
    - slot{"location": "Kanpur"}
    - slot{"price": [300.0, 500.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story 6383732568241984947
* restaurant_search{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - action_get_city
    - slot{"location": "Kanpur"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "4"}
    - slot{"option": ["4"]}
    - action_get_cuisine
    - slot{"cuisine": ["american"]}
    - utter_ask_price
* get_option{"option": "4"}
    - slot{"option": ["4"]}
    - action_get_price
* get_option{"option": "3"}
    - slot{"option": ["3"]}
    - action_get_price
    - slot{"price": [700, 10000]}
    - action_restaurant_search
    - slot{"cuisine": ["american"]}
    - slot{"location": "Kanpur"}
    - slot{"price": [700.0, 10000.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story 6383732568241984947
* restaurant_search{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - action_get_city
    - slot{"location": "Kanpur"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "4"}
    - slot{"option": ["4"]}
    - action_get_cuisine
    - slot{"cuisine": ["american"]}
    - utter_ask_price
* get_option{"option": "5"}
    - slot{"option": ["5"]}
    - action_get_price
* get_option{"option": "3"}
    - slot{"option": ["3"]}
    - action_get_price
    - slot{"price": [700, 10000]}
    - action_restaurant_search
    - slot{"cuisine": ["american"]}
    - slot{"location": "Kanpur"}
    - slot{"price": [700.0, 10000.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story 6383732568241984947
* restaurant_search{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - action_get_city
    - slot{"location": "Kanpur"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "4"}
    - slot{"option": ["4"]}
    - action_get_cuisine
    - slot{"cuisine": ["american"]}
    - utter_ask_price
* get_option{"option": "4"}
    - slot{"option": ["4"]}
    - action_get_price
* get_option{"option": "5"}
    - slot{"option": ["5"]}
    - action_get_price
* get_option{"option": "3"}
    - slot{"option": ["3"]}
    - action_get_price
    - slot{"price": [700, 10000]}
    - action_restaurant_search
    - slot{"cuisine": ["american"]}
    - slot{"location": "Kanpur"}
    - slot{"price": [700.0, 10000.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story 6383732568241984947
* restaurant_search{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - action_get_city
    - slot{"location": "Kanpur"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "4"}
    - slot{"option": ["4"]}
    - action_get_cuisine
    - slot{"cuisine": ["american"]}
    - utter_ask_price
* get_option{"option": "4"}
    - slot{"option": ["4"]}
    - action_get_price
* get_option{"option": "6"}
    - slot{"option": ["6"]}
    - action_get_price
* get_option{"option": "3"}
    - slot{"option": ["3"]}
    - action_get_price
    - slot{"price": [700, 10000]}
    - action_restaurant_search
    - slot{"cuisine": ["american"]}
    - slot{"location": "Kanpur"}
    - slot{"price": [700.0, 10000.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export


## Generated Story 5794089487774184057
* greet
    - utter_greet
* restaurant_search{"location": "gurugram"}
    - slot{"location": "gurugram"}
    - action_get_city
    - slot{"location": "Gurugram"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "6"}
    - slot{"option": ["6"]}
    - action_get_cuisine
    - slot{"cuisine": ["north indian"]}
    - utter_ask_price
* get_option
    - action_get_price
* get_option{"option": "3"}
    - slot{"option": ["3"]}
    - action_get_price
    - slot{"price": [700, 10000]}
    - action_restaurant_search
    - slot{"cuisine": ["north indian"]}
    - slot{"location": "Gurugram"}
    - slot{"price": [700.0, 10000.0]}
    - slot{"result_found": "yes"}
* affirm
    - utter_ask_email
* send_email{"email": "veer.tahin@gmail.com"}
    - slot{"email": ["veer.tahin@gmail.com"]}
    - action_send_email
    - slot{"email": ["veer.tahin@gmail.com"]}
    - action_restart
    - export

## Generated Story -3446382796654509538
* restaurant_search{"location": "bathinda"}
    - slot{"location": "bathinda"}
    - action_get_city
    - slot{"location": "bathinda"}
    - slot{"location_supported": "no"}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_get_city
    - slot{"location": "Bangalore"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "1"}
    - slot{"option": ["1"]}
    - action_get_cuisine
    - slot{"cuisine": ["chinese"]}
    - utter_ask_price
* get_option{"option": "2"}
    - slot{"option": ["2"]}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant_search
    - slot{"cuisine": ["chinese"]}
    - slot{"location": "Bangalore"}
    - slot{"price": [300.0, 700.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story -5327021984368430535
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": ["chinese"]}
    - utter_ask_location
* restaurant_search{"location": "moga"}
    - slot{"location": "moga"}
    - action_get_city
    - slot{"location": "moga"}
    - slot{"location_supported": "no"}
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_get_city
    - slot{"location": "Kolkata"}
    - slot{"location_supported": "yes"}
    - utter_ask_price
* get_option{"option": "2"}
    - slot{"option": ["2"]}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant_search
    - slot{"cuisine": ["chinese"]}
    - slot{"location": "Kolkata"}
    - slot{"price": [300.0, 700.0]}
    - slot{"result_found": "yes"}
* deny
    - utter_goodbye
    - action_restart
    - export

## Generated Story -5292559662274150494
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "price": "moderate"}
    - slot{"cuisine": ["mexican"]}
    - slot{"price": ["moderate"]}
    - utter_ask_location
* restaurant_search{"location": "pilani"}
    - slot{"location": "pilani"}
    - action_get_city
    - slot{"location": "pilani"}
    - slot{"location_supported": "no"}
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_get_city
    - slot{"location": "Hyderabad"}
    - slot{"location_supported": "yes"}
    - action_restaurant_search
    - slot{"cuisine": ["mexican"]}
    - slot{"location": "Hyderabad"}
    - slot{"price": [300.0, 700.0]}
    - slot{"result_found": "yes"}
* affirm
    - utter_ask_email
* send_email{"email": "p512uu@gmail.com"}
    - slot{"email": ["p512uu@gmail.com"]}
    - action_send_email
    - slot{"email": ["p512uu@gmail.com"]}
    - action_restart
    - export

## Generated Story 328739456911324436
* restaurant_search{"cuisine": "italian", "location": "bangalore"}
    - slot{"cuisine": ["italian"]}
    - slot{"location": "bangalore"}
    - action_get_city
    - slot{"location": "Bangalore"}
    - slot{"location_supported": "yes"}
    - utter_ask_price
* get_option{"option": "1"}
    - slot{"option": ["1"]}
    - action_get_price
    - slot{"price": [0, 300]}
    - action_restaurant_search
    - slot{"cuisine": ["italian"]}
    - slot{"location": "Bangalore"}
    - slot{"price": [0.0, 300.0]}
    - slot{"result_found": "no"}
    - action_restart
    - export

## Generated Story -5793138159988920147
* restaurant_search{"location": "pilani"}
    - slot{"location": "pilani"}
    - action_get_city
    - slot{"location": "pilani"}
    - slot{"location_supported": "no"}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_get_city
    - slot{"location": "Bangalore"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "3"}
    - slot{"option": ["3"]}
    - action_get_cuisine
    - slot{"cuisine": ["italian"]}
    - utter_ask_price
* get_option{"option": "1"}
    - slot{"option": ["1"]}
    - action_get_price
    - slot{"price": [0, 300]}
    - action_restaurant_search
    - slot{"cuisine": ["italian"]}
    - slot{"location": "Bangalore"}
    - slot{"price": [0.0, 300.0]}
    - slot{"result_found": "no"}
    - action_restart
    - export

## Generated Story -5277184384290765205
* restaurant_search{"price": "low", "location": "kolkata"}
    - slot{"location": "kolkata"}
    - slot{"price": ["low"]}
    - action_get_city
    - slot{"location": "Kolkata"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "1"}
    - slot{"option": ["1"]}
    - action_get_cuisine
    - slot{"cuisine": ["chinese"]}
    - action_restaurant_search
    - slot{"cuisine": ["chinese"]}
    - slot{"location": "Kolkata"}
    - slot{"price": [0.0, 300.0]}
    - slot{"result_found": "yes"}
* send_email{"email": "p512uu"}
    - slot{"email": ["p512uu"]}
    - action_send_email
    - slot{"email": ["p512uu"]}
    - utter_ask_email
* send_email{"cuisine": "p512uu"}
    - slot{"cuisine": ["p512uu"]}
    - utter_default
* send_email{"email": "p512uu@gmail.com"}
    - slot{"email": ["p512uu@gmail.com"]}
    - action_send_email
    - slot{"email": ["p512uu@gmail.com"]}
    - action_restart
    - export

## Generated Story -5277184384290765205
* restaurant_search{"price": "low", "location": "kolkata"}
    - slot{"location": "kolkata"}
    - slot{"price": ["low"]}
    - action_get_city
    - slot{"location": "Kolkata"}
    - slot{"location_supported": "yes"}
    - utter_ask_cuisine
* get_option{"option": "1"}
    - slot{"option": ["1"]}
    - action_get_cuisine
    - slot{"cuisine": ["chinese"]}
    - action_restaurant_search
    - slot{"cuisine": ["chinese"]}
    - slot{"location": "Kolkata"}
    - slot{"price": [0.0, 300.0]}
    - slot{"result_found": "yes"}
* send_email{"email": "p512uu"}
    - slot{"email": ["p512uu"]}
    - action_send_email
    - slot{"email": ["p512uu"]}
    - utter_ask_email
* send_email{"location": "abc"}
    - slot{"location": "abc"}
    - utter_default
* send_email{"email": "p512uu@gmail.com"}
    - slot{"email": ["p512uu@gmail.com"]}
    - action_send_email
    - slot{"email": ["p512uu@gmail.com"]}
    - action_restart
    - export














