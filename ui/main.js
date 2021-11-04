
const Board = {
  data() {
    return {
      num_cols:16,
      num_rows:16,
      list_walls:[]
    }
  },
  watch: {
     list_walls: {
        deep: true,
        handler(newValue) {
           localStorage['turtle-board'] = JSON.stringify({walls: newValue});
        }
     } 
  },
  methods: {
    wall(x,y){
        if (this.isWall(x,y)) {
           var l = this.list_walls.filter(([px,py]) => {
                return !((x == px) && (y == py))
            })
         this.list_walls = l        
         }    
        else 
            this.list_walls.push([x,y])  
    },
    isWall(x,y) {
        //some returns true iff [x,y] is in the list
        return this.list_walls.some(([px,py]) => {
            // [x,y] == [px,py]  <<< wrong!! in java strong
            return (x == px) && (y == py);
        })
    },
    clear() {
        this.list_walls = [];
    },
    go() {
      var toSend = JSON.stringify({walls: this.list_walls});
      console.log(toSend);
      fetch("/json",
        {
          method: "POST",
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          body: toSend
        });
    }
  }
}

var app = Vue.createApp(Board).mount('#Board')

var oldState = JSON.parse(localStorage['turtle-board'] || '{}');
if (oldState.walls)
    app.list_walls = oldState.walls;


/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


