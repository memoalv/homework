
/*
	File:		zebra.pl
	Purpose:	Solve the Zebra puzzle

	Notes:
	There are 5 houses, each of a different colour and inhabited by a
	man of a different nationality, with a different pet, drink and
	brand of cigarettes.

	1) The Englishman lives in the red house
	2) The Spaniard owns the dog
	3) Coffee is drunk in the green house
	4) The Ukrainian drinks tea
	5) The green house is immediately to the right (your right) of
	   the ivory house
	6) The Winston smoker owns snails
	7) Kools are smoked in the yellow house
	8) Milk is drunk in the middle house
	9) The Norwegian lives in the first house on the left
	10) The man who smokes Chesterfields lives in the house next to
	    the man with the fox
	11) Kools are smoked in the house next to the house where the
	    horse is kept
	12) The Lucky Strike smoker drinks orange juice
	13) The Japanese smokes Parliaments
	14) the Norwegian lives next to the blue house

    Q.	Who owns the Zebra?
	      Who drinks water?
*/

use_module( library(basics)).

use_module(library(lists)).

%
%	A street is a list of 5 houses; each house has a colour, a nationality
%	a pet, a drink, and a smoke.
%

street([house(_,_,_,_,_),
	house(_,_,_,_,_),
	house(_,_,_,_,_),
	house(_,_,_,_,_),
	house(_,_,_,_,_)] ).

%
%	We are told the following:
%
constraints( Street ) :-
	member(house(red, englishman, _, _, _), Street),	     % 1)
	member(house(_, spaniard, dog, _, _), Street),		      % 2)
	member(house(green, _, _, coffee, _), Street),	 	     % 3)
	member(house(_, ukrainian, _, tea, _), Street),		     % 4)
	nextto(house(ivory, _, _, _, _), house(green, _, _, _, _), Street), % 5)
	member(house(_, _, snails, _, winston), Street),	     % 6)
	member(house(yellow, _, _, _, kools), Street),		      % 7)
	Street = [_, _, house(_, _, _, milk, _), _, _],	     	% 8)
	Street = [house(_, norwegian, _, _, _)|_],		          % 9)
	perm2(Left_10, Right_10,
	     house(_, _, _, _, chesterfields), house(_, _, fox, _, _)),
	nextto(Left_10, Right_10, Street),			                  % 10)
	perm2(Left_11, Right_11,
		house(_, _, _, _, kools), house(_, _, horse, _, _)),
	nextto(Left_11, Right_11, Street),			                  % 11)
	member(house(_, _, _, orange, lucky_strike), Street),  % 12)
	member(house(_, japaNese, _, _, parliaments), Street),	% 13)
	perm2(Left_14, Right_14,
	     house(_, norwegian, _, _, _), house(blue, _, _, _, _)),
	nextto(Left_14, Right_14, Street),			                  % 14)
	\+ member(house(yellow, _, _, _, parliaments), Street).

%
%	Who owns the Zebra?
%
zebra( Who ) :-
	street(Street),
	constraints(Street),
	member(house(_, Who, zebra, _, _), Street).

%
%	Who drinks water?
%
water( Who ) :-
	street(Street),
	constraints(Street),
	member(house(_, Who, _, water, _), Street).
	
	

nextto(X, Y, List) :- append(_, [X,Y|_], List).

append([X|Y],Z,[X|W]) :- append(Y,Z,W).  
append([],X,X).

member(X,[X|T]).
member(X,[H|T]) :- member(X,T).

%   perm2(A,B, C,D)
%   is true when {A,B} = {C,D}.  It is very useful for writing pattern
%   matchers over commutative operators.  It is used more than perm is.
 
perm2(X,Y, X,Y).
perm2(X,Y, Y,X).
