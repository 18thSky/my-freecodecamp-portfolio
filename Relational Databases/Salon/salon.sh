#! /bin/bash

PSQL="psql -X --username=freecodecamp --dbname=salon --tuples-only -c"
echo -e "\n~~~~~ MY SALON ~~~~~\n"

MAIN_MENU() {
  # Print the custom message if one is passed in, otherwise print the default greeting
  if [[ $1 ]]
  then
    echo -e "\n$1"
  else
    echo "Welcome to My Salon, how can I help you?"
  fi

  # Get available services
  AVAILABLE_SERVICES=$($PSQL "SELECT service_id, name FROM services ORDER BY service_id")

  # Display available services
  echo "$AVAILABLE_SERVICES" | while read SERVICE_ID BAR NAME
  do
    echo "$SERVICE_ID) $NAME"
  done

  # Ask for service
  read SERVICE_ID_SELECTED

  # Check if input is not a number
  if [[ ! $SERVICE_ID_SELECTED =~ ^[0-9]+$ ]]
  then
    MAIN_MENU "I could not find that service. What would you like today?"
  else
    # Check if the specific service exists in the database
    SERVICE_AVAILABILITY=$($PSQL "SELECT name FROM services WHERE service_id = $SERVICE_ID_SELECTED")

    # If service doesn't exist
    if [[ -z $SERVICE_AVAILABILITY ]]
    then
      # Send back to main menu
      MAIN_MENU "I could not find that service. What would you like today?"
    else
      # Placeholder for the next step
      echo -e "\nWhat's your phone number?"
      read CUSTOMER_PHONE
      CUSTOMER_NAME=$($PSQL "SELECT name FROM customers WHERE phone = '$CUSTOMER_PHONE'")

      if [[ -z $CUSTOMER_NAME ]]
      then
      echo -e "I don't have a record for that phone number, what's your name?"
      read CUSTOMER_NAME
      INSERT_CUSTOMER_RESULT=$($PSQL "INSERT INTO customers(name,phone) VALUES('$CUSTOMER_NAME','$CUSTOMER_PHONE')")
      else 
      echo "Welcome back!"
    fi

    CUSTOMER_ID=$($PSQL "SELECT customer_id FROM customers WHERE phone = '$CUSTOMER_PHONE'")
    echo -e "\n What time would you like your $SERVICE_AVAILABILITY, $CUSTOMER_NAME?"
    read SERVICE_TIME
    INSERT_APPOINTMENT_RESULT=$($PSQL "INSERT INTO appointments(customer_id,service_id,time) VALUES('$CUSTOMER_ID','$SERVICE_ID_SELECTED','$SERVICE_TIME')")
    echo -e "\nI have put you down for a $(echo $SERVICE_AVAILABILITY) at $SERVICE_TIME, $(echo $CUSTOMER_NAME)."
  fi
  fi
}

MAIN_MENU
    
    # do
    #   echo "$BIKE_ID) $SIZE\" $TYPE Bike"
    # done

#     #ask for bike to rent
#     echo -e "\nWhich one would you like to rent?"
#     read BIKE_ID_TO_RENT

#     #if input is not a number
#     if [[ ! $BIKE_ID_TO_RENT =~ ^[0-9]+$ ]]
#     then
#     #send to main menu
#     MAIN_MENU "That is not a valid bike number."
#     else
#     #get bike availability
#     BIKE_AVAILABILITY=$($PSQL "SELECT available from bikes WHERE bike_id = $BIKE_ID_TO_RENT AND available = true;")
#     # echo "$BIKE_AVAILABILITY"
#     #if not available
#     if [[ -z $BIKE_AVAILABILITY ]]
#     then
#       #send to main menu
#       MAIN_MENU "That bike is not available."
    
#     else
#     #get customer info
#     echo -e "\nWhat's your phone number?"
#     read PHONE_NUMBER
#     CUSTOMER_NAME=$($PSQL "SELECT name FROM customers WHERE phone = '$PHONE_NUMBER'")
#     #if customer doesn't exist
#     if [[ -z $CUSTOMER_NAME ]]
#     then
#     #get new customer name
#     echo -e "\nWhat's your name?"
#     read CUSTOMER_NAME 
#     #insert new customer
#     INSERT_CUSTOMER_RESULT=$($PSQL "INSERT INTO customers(name,phone) VALUES('$CUSTOMER_NAME','$PHONE_NUMBER');")
#     fi
#     # get customer_id
#     CUSTOMER_ID=$($PSQL "SELECT customer_id from customers WHERE phone ='$PHONE_NUMBER';")
#     # insert bike rental
#     INSERT_RENTAL_RESULT=$($PSQL "INSERT INTO rentals(bike_id,customer_id) VALUES('$BIKE_ID_TO_RENT','$CUSTOMER_ID');")
#     # set bike availability to false
#     SET_TO_FALSE_RESULT=$($PSQL "UPDATE bikes SET available = false WHERE bike_id = '$BIKE_ID_TO_RENT';")
#     # get bike info
#     BIKE_INFO=$($PSQL "SELECT size,type from bikes WHERE bike_id = '$BIKE_ID_TO_RENT';")
#     BIKE_INFO_FORMATTED=$(echo $BIKE_INFO | sed 's/ |/"/')
#     # send to main menu
#     MAIN_MENU "I have put you down for the $BIKE_INFO_FORMATTED Bike, $(echo $CUSTOMER_NAME | sed -r 's/^ *| *$//g')."
    
#     fi
#     fi
#   fi
# }
# }