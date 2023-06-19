<script>

    import { onDestroy, onMount } from 'svelte';

    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();

    export let state_ctrl;

    export let date;

    export let page3_next_allow = false;
    dispatch('change', page3_next_allow);

    export let page4_next_allow = false;
    dispatch('change', page4_next_allow);

    export let page5_next_allow = false;
    dispatch('change', page5_next_allow);

    let next_after_play_p3 = false;
    let next_after_play_p4 = false;
    let next_after_play_p5 = false;

    let stream;
    let mediaRecorder;
    let recordButton;
    let chunks = [];
    let clips = [];
    let state = "waiting";
    
    let rec_icon = '<img width=70 height=70 src="./img/gravar.png">';

    function onStop(e) {
        console.log("recorder stopped");
        console.log(chunks);

        const blob = new Blob(chunks, {type: "audio/mpeg"});
        chunks = [];

        const audioURL = window.URL.createObjectURL(blob);
        console.log(audioURL);

        clips = [
            {
                ...clips,
                src: audioURL,
            },
        ];
        console.log(clips);

        ///////////////////////////////////

        let audioData = new FormData();
        audioData.append('audio', blob, '{}_audioRec_{}.wav'.format(date , state_ctrl-1));

        console.log("VVVVVVV Audio data: ", audioData);
        fetch('http://localhost:5000/upload-audio', {
            mode: 'cors',
            method: 'POST',
            body: audioData,})
        .then((response) => response.json());        
    }

    async function setup() {
        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
            console.log("getUserMedia supported.");
            stream = await navigator.mediaDevices.getUserMedia({audio: true});
            
            mediaRecorder = new MediaRecorder(stream, {mimeType: 'audio/webm'});
                mediaRecorder.ondataavailable = (e) => {
                    if (e.data.size > 0) chunks.push(e.data);
                }
            mediaRecorder.onstop = onStop;
        }
    }

    onMount(async () => setup());

    function record() {
        console.log("recorder started");
        state="recording"
        mediaRecorder.start();

        if (state_ctrl == 2){
            next_after_play_p3 = true;            
        }

        if (state_ctrl == 3){
            next_after_play_p4 = true;            
        }

        if (state_ctrl == 4){
            next_after_play_p5 = true;            
        }
        
        rec_icon = '<img width=70 height=70 src="./img/gravar_off.png">';
    }

    function stop() {
        state="sending"
        mediaRecorder.stop();
        console.log(mediaRecorder.state);
        console.log("recorder stopped");
        
        rec_icon = '<img width=70 height=70 src="./img/gravar.png">';

        if (state_ctrl == 2 && next_after_play_p3 == true){
            page3_next_allow = true;
        }

        if (state_ctrl == 3 && next_after_play_p4 == true){
            page4_next_allow = true;
        }

        if (state_ctrl == 4 && next_after_play_p5 == true){
            page5_next_allow = true;
        }
    }

    String.prototype.format = function () {
        var i = 0, args = arguments;
        return this.replace(/{}/g, function () {
            return typeof args[i] != 'undefined' ? args[i++] : '';
        });
    };

</script>


<!--
<p>Página _recorder show_: {state_ctrl}</p>
<p>Data _recorder show_: {date}</p>

<p>page3_next_allow RECORD: {page3_next_allow}</p>
<p>page4_next_allow RECORD: {page4_next_allow}</p>
<p>page5_next_allow RECORD: {page5_next_allow}</p>
-->

<div class="container max-auto px-10 w-full">
    <div class="flex justify-items-center text-center">
        <div class="flex flex-col justify-center mx-auto text-center">
            
            <!--
            <div class="text-white h-8 mb-10">
                {#if state=="waiting"}
                    <p></p>
                    <!-- <img class="animate-spin" src="img/loading.svg" alt="Loading" width=40 height=40>
                {:else if state=="recording"}
                    <p></p>
                    <!-- <img class="animate-spin" src="img/loading.svg" alt="Loading" width=40 height=40>
                {:else if state=="sending"}
                    <img 
                        class="animate-spin mx-auto justify-center" 
                        src="img/loading.svg" 
                        alt="Loading" width=40 height=40>
                    <!-- <p>Enviando</p>
                {:else}
                    <p></p>
                {/if}    
            </div>
            -->

            <spacing>-</spacing>
            <br>

            <div id="buttons" class="mx-auto h-28">
                <button class="button_style"   on:click={record} bind:this={recordButton}> {@html rec_icon} </button>
                <button class="button_style"   on:click={stop}>                            <img width=70 height=70 src="./img/parar.png"> </button>
            </div>

            <spacing>-</spacing>
            <br>
            
        </div>
    </div>
</div>



<style>
	.button_style {
		padding: 0;
		border: none;
		background: none;
	}

    spacing {
		color: #ffffff;		
		font-size: 1em;
	}
</style>