# tribbekR - Capstone Proposal

### in the words of Alex Trebek
>I'm curious about everything. Even subjects that don't interest me.

## What is tribbekR?
Seems that every successful app ends with a capitol R, and as tribute to the king of trivia, we named our trvia hosting app as "tribbekR". We wanted to stand out by fitting in!

tribbekR is a go-to app for your trivia hosting needs. Anyone can be a host with variety of topics at your fingertips. At home or at a bar, or even a coding class if you wish, can be turned into a trvia game!

## Project Overview
The host user will be able to set up a trvia game in variety of sources for questions in one time or league setting where point data will remain in history for future access/multiple event. We hope to use websocket to facilitate real time access to the hosted trivia by players/teams in their own mobile devices to submit their answers. The application will reward points to the winners with options for hosts to override in case of disputes.

## Functionality
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

## Data Model
[data model for tribbekR](ProposalItems/Capston%20Proposal%20-%20Process%20Map.png)
*Core Process
 -1. User - Host creation
 -2. Game session creation
     -1. Define settings for game
     -2. Pull data from API (category/questions)
 -3. Completion/Show cumulative data
*Multi Session Support
 -1. Settings/Points awards preseved for set/unset future sessions
     -1. Save host inputed player data/points
     -2. Ability to resume
     -3. Ability to add sessions
*Custom Gane Support
 -1. Model to hold custom questions
    *User - Host will have access
*Player Implementation Support (Unknown process - websockets)
 -1. User - Player creation ability
 -2. User - Player log in
    -*Track past points/wins
 -3. REAL TIME ANSWER SUBMISSION SUPPORT
    -*Currently insufficient knowledge for the developer - Wish to accomplish

## Schedule

### Week 1
-[ ]Develop Core Functions
    - [ ]"storyboard" for visual mock up for Process Map
    - [ ]User - Host model set up
    - [ ]Game Setup
    - [ ]Sources/API
    - [ ]Complete 1 game

### Week 2
-[ ]Multi-Session Implementation
    -[ ]Model for game preservation
    -[ ]Setting for multiple/league mode
-[ ]Custom Game Implementation
    -[ ]Model for User - Host input category
    -[ ]Input/Review interface

### Week 3
-[ ]Player Implementation
    -[ ]Model for player
    -[ ]Login/Logout interface
    -[ ]Player Profile/Past Scores
    -[ ]Real-time answer submit by Player
        -[ ]Websocket(???)
        -[ ]Interface for submition - Simple A-D/E boxes and T/F boxes

### Week 4
-[ ]Extra time in case of bottleneck/implement "wishlist" items
-[ ]Presentation Prep
    -[ ]Determine Flow of the presentation
    -[ ]Tell a story
    -[ ]Insure following are noted
      - [ ]User States
      - [ ]API's Used
      - [ ]Custom Abilities
      - [ ]Multi-Session
      - [ ]User - Player Experience
      - [ ] (Room to edit)

### Wishlist/Future Implementation
-[ ]DETAILED Answer boxes pushed to User Devices
-[ ]Easy code based login/play - Single Instance - No Save Data
-[ ]Smooth exchanges in interface
 