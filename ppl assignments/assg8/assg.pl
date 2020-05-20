flight(toronto, aircanada, london, 500, 360).
flight(london, aircanada, toronto, 500, 360).

flight(toronto, united, london, 650, 420).
flight(london, united, toronto, 650, 420).

flight(toronto, aircanada, madrid, 900, 480).
flight(madrid, aircanada, toronto, 900, 480).

flight(toronto, united, madrid, 950, 540).
flight(madrid, united, toronto, 950, 450).

flight(toronto, iberia, madrid, 800, 480).
flight(madrid, iberia, toronto, 800, 480).

flight(london, iberia, barcelona, 220, 240).
flight(barcelona, iberia, london, 220, 240).

flight(madrid, aircanada, barcelona, 100, 60).
flight(barcelona, aircanada, madrid, 100, 60).

flight(madrid, iberia, barcelona, 120, 65).
flight(barcelona, iberia, madrid, 120, 65).

flight(barcelona, iberia, valenica, 110, 75).
flight(valenica, iberia, barcelona, 110, 75).

flight(madrid, iberia, valenica, 40, 50).
flight(valenica, iberia, madrid, 40, 50).

flight(madrid, iberia, malaga, 50, 60).
flight(malaga, iberia, madrid, 50, 60).

flight(malaga, iberia, valenica, 80, 120).
flight(valenica, iberia, malaga, 80, 120).

flight(paris, united, toulouse, 35, 120).
flight(toulouse, united, paris, 35, 120).

airport(toronto, 50, 60).
airport(london, 75, 80).
airport(madrid, 75, 45).
airport(barcelona, 40, 30).
airport(malaga, 50, 30).
airport(valenica, 40, 20).
airport(paris, 50, 60).
airport(toulouse, 40, 30).

is_flight(A, B) :-
    flight(A, X, B, Y, Z).

is_cheap(A, B) :-
    flight(A, C, B, X, Y), X < 400.

two_flights(A, B):-
   ( flight(A, X, B, Y, Z), flight(A, P, B, Q, R)).

its_prefered(A, B) :-
    (flight(A, C, B, X, Y) ), ( X < 400 ; C = aircanada).

then_flight(A, B) :-
    (flight(A, C, B, X, Y) , C = united) -> (flight(A, P, B, Q, R), P = aircanada).

