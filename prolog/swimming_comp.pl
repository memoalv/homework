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

use_module( library(basics)).
use_module(library(lists)).

member(X,[X|T]).
member(X,[H|T]) :- member(X,T).

teams([
	camp(_,_,_,_,relayRace),
	camp(_,rand,_,_,_),
	camp(_,_,_,green,_),
	camp(dan,_,_,_,_)
]).

constraints( Team ) :-
		% 1
		member(camp(sam, brown, _, _, _), Team),

		member(camp(_, smart, forestRidge, _, _), Team),
		% 2
		member(camp(_, _, woodlandPark, red, _), Team),
		% 3
		member(camp(mark, _, _, purple, _), Team),
		% 4
		member(camp(_, _, wildRiver, _, oneMileRace), Team).
		% neg
		% 1
		% \+ member(camp(sam, brown, woodlandPark, _, _), Team),
		% \+ member(camp(sam, brown, _, purple, _), Team),
		% \+ member(camp(sam, brown, _, purple, _), Team),
		% \+ member(camp(dan, _, forestRidge, _, _), Team),
		% % 3
		% \+ member(camp(mark, manor, _, _, _), Team),
		% \+ member(camp(mark, smart, _, _, _), Team),
		% \+ member(camp(_, _, lakeside, _, divingComp), Team),
		% % 4
		% \+ member(camp(_, _, forestRidge, red, _), Team),
		% \+ member(camp(_, _, forestRidge, blue, _), Team),
		% \+ member(camp(bill, _, _, _, freestyleRace), Team).


		%%%%%%%%%%%%%%%%%
		% member(camp(_, _, _, _, relayRace), Team),
		% member(camp(_, rand, _, _, _), Team),
		% member(camp(_, _, _, green, _), Team),
		% member(camp(dan, _, _, _, _), Team),
		
who(X) :- 
		teams(Team),
		constraints(Team),
		member(camp(X, brown, _, _, _), Team).
		