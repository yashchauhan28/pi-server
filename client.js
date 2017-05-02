"use strict";

var client = {
    queue: {},
    led_on: false,

    connect: function (port) {
        var self = this;
        this.socket = new WebSocket("ws://" + window.location.hostname + ":" + port + "/websocket");

        this.socket.onopen = function () {
            console.log("Connected!");
        };

        this.socket.onmessage = function (messageEvent) {
            var router, current, updated, jsonRpc;

            jsonRpc = JSON.parse(messageEvent.data);
            router = self.queue[jsonRpc.id];
            delete self.queue[jsonRpc.id];
            self.result = jsonRpc.result;

            if (jsonRpc.error) {
                alert(jsonRpc.result);
            } else if (router === "toggle_led") {
                $(".answer").html("LED is currently " + (self.led_on ? "on" : "off") + ".");
            } else if(router=="send_message"){
                $(".answer").html("message sent..");
            }else {
                alert("Unsupported function: " + router);
            }
        };
    },

    // Generates a unique identifier for request ids
    // Code from http://stackoverflow.com/questions/105034/
    // how-to-create-a-guid-uuid-in-javascript/2117523#2117523
    uuid: function () {
        return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
            var r = Math.random()*16|0, v = c == 'x' ? r : (r&0x3|0x8);
            return v.toString(16);
        });
    },

    // Sends a message to toggle the LED
    toggle_led: function () {
        this.led_on = !this.led_on;
        var uuid = this.uuid();
        this.socket.send(JSON.stringify({method: "toggle_led", id: uuid, params: {on: this.led_on}}));
        this.queue[uuid] = "toggle_led";
        console.log("Hello");
    },

    //Catches input
    send_message: function(input_string){
        console.log(input_string);
        var uuid = this.uuid();
        this.socket.send(JSON.stringify({method: "send_message", id: uuid, params: {text: input_string}}));
        this.queue[uuid] = "send_message";
        //console.log("send message");
    }
};
