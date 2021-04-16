
Vue.use(Vuex);


// import { mapState } from 'vuex';
const value1 = JSON.parse(document.getElementById('json-data').textContent);




console.log(value1)
var app1 = new Vue({
    delimiters: ['[[',']]'],
    el: '#trivia',
    data: {
        total_questions: 0,
        questions: {},
        currquestion_num: 0,
        currquestion: '',
        currtruefalse: null,
        curranswers: [],
        currcorrect_answer: '',
        player_data: [
            {
                player_name: '',
                score: 0,
                answers: {},
            },
            {
                player_name: '',
                score: 0,
                answers: {},
            },
            {
                player_name: '',
                score: 0,
                answers: {},
            },
            {
                player_name: '',
                score: 0,
                answers: {},
            },
            {
                player_name: '',
                score: 0,
                answers: {},
            },
            {
                player_name: '',
                score: 0,
                answers: {},
            },
            {
                player_name: '',
                score: 0,
                answers: {},
            },
            {
                player_name: '',
                score: 0,
                answers: {},
            },
        ]
        
    },
    methods: {
        updateQuestion (question_num){
            console.log("got to vue")
            this.currquestion_num = question_num

            this.currquestion = this.decodeHtml(this.questions[question_num-1].question)
            this.currcorrect_answer = this.questions[question_num-1].answer
            this.currtruefalse = this.questions[question_num-1].truefalse
            if (this.currtruefalse == true){
                this.curranswers = [
                    true,
                    false
                ]
            } else{
                this.curranswers = [
                    this.questions[question_num-1].wrong1,
                    this.questions[question_num-1].wrong2,
                    this.questions[question_num-1].wrong3,
                    this.questions[question_num-1].answer
                ]
                this.curranswers = this.curranswers
                console.log(this.curranswers)
                this.shuffle(this.curranswers)
                console.log(this.curranswers)

            }
        },
        decodeHtml: function(html) {
            let areaElement = document.createElement("textarea");
            areaElement.innerHTML = html;
        
            return areaElement.value;
        },

        startGame: function(event) {
            console.log('start')
            // Game div should be visible after starting
            let game = document.getElementById("game")
            game.style.display = "inline"
     
            //let player_div = document.getElementById('players-list')
            //let count = player_div.childElementCount
            //console.log(count)
        
            
            //let players = player_div.children
            //console.log(players)
            
            // for ( let player of players){
            //     console.log('next is number')
            //     let player_num = player.name
            //     // console.log(player_num)
            //     let player_name = player.value;

            //     let player_data = []
            //     player_data[0] = player_num
            //     player_data[1] = player_name
            //     console.log(player_data)

            //     // let player_name = player_split[1]
            //     this.$store.commit('initial_users', player_data)
            //     // this.$store.commit('addUserName', player_num, player_name);
            //     updateQuestion(1)
            // }
            this.updateQuestion(1)
            console.log(this.currquestion_num)
            console.log(this.currquestion)
            console.log(this.currtruefalse)
            console.log(this.curranswers)
            console.log(this.currcorrect_answer)

            event.target.hidden = "true"

        },




        nextQuestion: function(event) {
            let multi_button = event.target

            if (multi_button.innerText == "Next"){

                // button to Show Answers
                multi_button.innerText = "Show Answers!"

                // reset answers properties
                let  choices = document.getElementsByClassName("answers")
                console.log(choices)

                // rug through to see which is right
                for ( const choice of choices) {
                    if (choice.innerText == this.currcorrect_answer){
                        choice.style.cssText = ""
                    }
                };

  
                this.updateQuestion(this.currquestion_num + 1)
            } else if (multi_button.innerText === "Show Answers!" ){

                // get all answer items
                let  choices = document.getElementsByClassName("answers")
                console.log(choices)

                // rug through to see which is right
                for ( const choice of choices) {
                    if (choice.innerText == this.currcorrect_answer){
                        choice.style.cssText = "color:red;font-weight:bolder"
                    }
                };
                
                // button to Next or Done
                if (this.currquestion_num == this.total_questions){
                    multi_button.innerText = "Done"
                    console.log(event.target)
                } else {
                    multi_button.innerText = "Next"
                }
            }},

        shuffle: function(array) {
            var currentIndex = array.length, temporaryValue, randomIndex;
          
            // While there remain elements to shuffle...
            while (0 !== currentIndex) {
          
              // Pick a remaining element...
              randomIndex = Math.floor(Math.random() * currentIndex);
              currentIndex -= 1;
          
              // And swap it with the current element.
              temporaryValue = array[currentIndex];
              array[currentIndex] = array[randomIndex];
              array[randomIndex] = temporaryValue;
            }
          
            return array;
        },
    },
    created: function() {
        // Game div should be hidden on start
        let game = document.getElementById("game")
        game.style.display = "none"
        this.total_questions = value1.length
 
        this.questions = value1

        console.log(this.questions[0].answer)

        console.log(this.player_data)
 

    }
})
