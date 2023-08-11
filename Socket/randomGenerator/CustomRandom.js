const hash = require('./hash');
const sfc32 = require('./sfc32');

class Random{

    constructor(str){
        this.seed = str;
        this.hashedSeed = hash(this.seed);
        this.randFunction = sfc32(this.hashedSeed[0], this.hashedSeed[1], this.hashedSeed[2], this.hashedSeed[3]);
    }

    getRandom(){
        return this.randFunction();
    }

    getRandomOption(options){
        return options[Math.floor(this.getRandom() * options.length)];
    }
}

module.exports = Random;