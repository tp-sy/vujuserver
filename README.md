    # Login
    /otit32/login?user_id=<userid|str>
    RESPONSE: HTTP 200 "Ok"

    # Order
    /otit32/order?user_id=<userid|str>&product_id=<productid>
    RESPONSE: HTTP 200 "Ok"

    # Confirm order received
    /otit32/received?user_id=<userid|str>
    RESPONSE: HTTP 200 "Ok"


    # Get all upcoming songs
    /otit32/songs/upcoming?user_id=<userid|str>
    RESPONSE: Json {
        'results': [
            {
                'song_id': song id,
                'song_time': hh:mm,
                'user_id': user_id
            },
            ...
            ]
        }


    # Requests a song
    /otit32/songs/request?user_id=<userid|str>&song_id=<songid|int>&time=<hour:minute|str>
    RESPONSE: HTTP 200 "Ok"

    # Get all users
    /otit32/all_users
    RESPONSE: Json {
        'results': [
            {
                'user_id': user_id,
                'order_id': order_status,
                'present': present
            },
            ...
            ]
        }

    # Get info for one user
    /otit32/user?user_id=<userid|str>
    RESPONSE: Json {
        'results': {
                'user_id': user_id,
                'order_id': order_status,
                'present': present
            }
        }