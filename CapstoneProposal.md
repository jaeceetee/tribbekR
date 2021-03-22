# tribbekR - Capstone Proposal

###in the words of Alex Trebek
>I'm curious about everything. Even subjects that don't interest me.

##What is tribbekR?
Seems that every successful app ends with a capitol R, and as tribute to the king of trivia, we named our trvia hosting app as "tribbekR". We wanted to stand out by fitting in!

tribbekR is a go-to app for your trivia hosting needs. Anyone can be a host with variety of topics at your fingertips. At home or at a bar, or even a coding class if you wish, can be turned into a trvia game!

##Project Overview
The host user will be able to set up a trvia game in variety of sources for questions in one time or league setting where point data will remain in history for future access/multiple event. We hope to use websocket to facilitate real time access to the hosted trivia by players/teams in their own mobile devices to submit their answers. The application will reward points to the winners with options for hosts to override in case of disputes.

##Functionality
*Users
 -1. User/s - Host
     -1. Create games
     -2. Oversee games
     -3. Manage points as needed
     -4. Manage users as needed
 -2. Users - Player
     -1. Access games
     -2. Submit answers
*Games
 -1. Use API to gather topics/sources
 -2. Use API to gather questions on chosen topic/sources
 -3. Structure games with data, preserving user points
 -4. Multi-session allowed (league mode)
