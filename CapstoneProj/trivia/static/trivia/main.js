import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const store = Vuex.Store({
    state: {
        total_question: 0,
        question_num: 0,
        question: '',
        truefalse: null,
        answers: [],
    }
})

let app1 = new Vue({
    el: '#trivia',
    delimiters: [ '<%', '%>'],
    data: {
        total_question: 0,
        question_num: 0,
        question: '',
        truefalse: null,
        answers: [],

    },
    methods: {
        // nextQuestion: async function() {
        //     let response = await axios({
        //         method: 'get',
        //         url: 
        //     })
            
        // }

    },
    created: function() {


    }
})

let player_list = new Vue ({
    el: '#players',
    delimiters: [ '<%', '%>'],
    data: {
        players: []
    }
})
