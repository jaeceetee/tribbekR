
Vue.use(Vuex);


// import { mapState } from 'vuex';
const value1 = JSON.parse(document.getElementById('json-data').textContent);
console.log(value1)
let app1 = new Vue({
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
        
    },
    methods: {
        updateQuestion (question_num){
            console.log("got to vue")
            this.currquestion_num = question_num
            this.currquestion = this.questions[question_num-1].question
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
            }
        },

        startGame: function(event) {
            console.log('start')
     
            let player_div = document.getElementById('players-list')
            //let count = player_div.childElementCount
            //console.log(count)
        
            
            let players = player_div.children
            //console.log(players)
            
            for ( let player of players){
                console.log('next is number')
                let player_num = player.name
                // console.log(player_num)
                let player_name = player.value;

                let player_data = []
                player_data[0] = player_num
                player_data[1] = player_name
                console.log(player_data)

                // let player_name = player_split[1]
                this.$store.commit('initial_users', player_data)
                // this.$store.commit('addUserName', player_num, player_name);
                updateQuestion(1)
            }
            this.updateQuestion(1)
            console.log(this.currquestion_num)
            console.log(this.currquestion)
            console.log(this.currtruefalse)
            console.log(this.curranswers)
            console.log(this.currcorrect_answer)

            event.srcElement.hidden = "true"

        },

        nextQuestion: function(event) {
            if (event.srcElement.innerText == "Done"){
                console.log("Completed Page")
            } else {
                this.updateQuestion(this.currquestion_num + 1)
                if (this.currquestion_num == this.total_questions){
                    event.srcElement.innerText = "Done"
                    console.log(event.srcElement)
                }

            }
        },
        showAnswers: function (event) {
            console.log(this.currtruefalse);
            if (this.currtruefalse == "true"){
                let multiple = document.getElementById("multiple")
                console.log(multiple)
                for (choice of multiple) {
                    console.log(choice)
                }
            }
        }
                
    },
    created: function() {
        this.total_questions = value1.length
        this.questions = value1

        console.log(this.questions[0].answer)
 

    }
})
