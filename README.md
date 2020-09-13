    # Login
    /otit32/login?user_id=<userid|str>
    
    # Order
    /otit32/order?user_id=<userid|str>&product_id=<productid>
    
    # Confirm order received
    /otit32/received?user_id=<userid|str>
    
    # Get all upcoming songs
    /otit32/songs/upcoming?user_id=<userid|str>
    
    # Requests a song
    /otit32/songs/request?user_id=<userid|str>&song_id=<songid|int>&time=<hour:minute|str>