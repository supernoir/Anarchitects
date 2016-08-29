'use strict'

var expect = require('chai').expect;


describe('SETUP -- Mocha', function() {
   it('should run our tests using npm', function() {
      expect(true).to.be.ok;
   });
});

describe('SERVER -- Started', function(){
   it('should listen on port 3030', function() {
       var server = require('../server.js');
           expect(server.startServer()).to.equal(3030); 
      });	       
});

