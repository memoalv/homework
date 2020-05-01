/*
	Last weekend, the Woodland Boys summer camp hosted their annual swim meet
	with their rivals, the Lakeside Boys camp, the Wild River camp, and the 
	Forest Ridge camp. The swim meet lasted all day and involved several events,
	which each camp team participated in. This meet was very exciting since each
	team broke a meet record for a different event. In the history of the camp 
	event, never had four records been broken at a single meet. From the clues 
	below, determine the full name of each team captain, the camp each team was
	from, the team's colors, and the event each team broke the record for. 

	1. Sam Brown was not the team captain from the Woodland Park Camp and his 
		team was not wearing purple. The Forest Ridge camp, which Dan was not
		with, was Mr. Smart's camp. 
	2. The Woodland Park Camp team colors were red. 
	3. Mark, whose last name was not Manor or Smart, was the captain of the 
		purple team. The Lakeside camp team did not win the diving competition. 
	4. The Forest Ridge camp colors were not red or blue. The Wild River Camp
		team won the 1- mile race. 
	5. Bill's team did not win the freestyle race. 
	6. The four camps are represented by: the camp that won the relay race, 
		Mr. Rand's team, the green team, and Dan's team.
*/

:- use_module(library(clpfd)).

main() :- 
    Tables = [TeamCapFirstName, TeamCapLastName, TeamColor, Event],

    ForestRidge = 1, WoodlandPark = 2, WildRiver = 3, Lakeside = 4,
    TeamCapFirstName = [Dan, Bill, Sam, Mark],
    TeamCapLastName = [Smart, Manor, Brown, Rand],
    TeamColor = [Blue, Red, Green, Purple],
    Event = [Freestyle, Relay, OneMile, DrivingComp],

    % 1
    Sam #= Brown,
    Sam #\= WoodlandPark,
    Sam #\= Purple,
    Dan #\= ForestRidge,
    Smart #= ForestRidge,

    % 2
    WoodlandPark #= Red,

    % 3
    Mark #\= Manor,
    Mark #\= Smart,
    Mark #= Purple,
    Lakeside #\= DrivingComp,

    % 4
    ForestRidge #\= Red,
    ForestRidge #\= Blue,
    WildRiver #= OneMile,

    % 5
    Bill #\= Freestyle,

    % 6
    Rand #\= Relay,
    Rand #\= Green,
    Rand #\= Dan,
    Relay #\= Green,
    Relay #\= Dan,
    Dan #\= Green,

    append(Tables, Vs),
    Vs ins 1..4,
    maplist(all_distinct, Tables),
    label(Vs),
    /*
        Los arreglos que el programa imprime son los equipos
        que corresponden para esa posición del arreglo.

        Ejemplo: 
        Equipos: ForestRidge = 1, WoodlandPark = 2, WildRiver = 3, Lakeside = 4
        Arreglo inicial: TeamCapFirstName = [Dan, Bill, Sam, Mark]
        Arreglo final: [2,1,4,3]
        
        Dan pertenece al equipo de WoodlandPark
        Bill pertenece al equipo ForestRidge
        Sam pertenece al aquipo Lakeside
        Mark pertenece al equipo WildRiver
    */
    write(TeamCapFirstName), nl,
    write(TeamCapLastName), nl,
    write(TeamColor), nl,
    write(Event), nl.