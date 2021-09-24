new Vue({
    el: '#films',
    data: {
    films: []
    },
    created: function() {
        const app = this;
        axios.get('/api/films/').then(function(response) {
            app.films = response.data;
        })
    }
})