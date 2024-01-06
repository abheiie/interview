## Usecase Diagram 
    @startuml
    """

    !theme amiga
    left to right direction

    actor User
    actor Admin

    rectangle Academy {
        usecase "Add movie" as add_movie
        usecase "Add theater" as add_theater
        usecase "search" as search 
        usecase "book" as book
        usecase "upi" as upi
        usecase "net banking" as net_banking
        usecase "pay" as pay
        usecase "check availibility" as check_availibility
        usecase "by name" as by_name
        usecase "by theater" as by_theater


        (pay) .> (upi) : extends
        (pay) .> (net_banking) : extends
        (book) .> (check_availibility) : includes 
        (search) .> (by_name) : extends
        (search) .> (by_theater) : extends

        
        usecase "cancel" as cancel
        
    }

    Admin --> add_movie
    Admin --> add_theater



    User --> search
    User --> book
    User --> pay
    User --> cancel


    """
    @enduml
