<script>
	import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
	
	function next_state (){
        cur_state += 1;
        dispatch('increment', cur_state);
    }	

	function back_state (){
        cur_state -= 1;
        dispatch('increment', cur_state);
    }

    export let state_ctrl;

    let cur_state = state_ctrl;

	export let page3_next_allow;
    export let page4_next_allow;
    export let page5_next_allow;
    
</script>


<!--
<p>cur_state _NEXT_BACK_: {state_ctrl+1}</p>
<p>Data page3_next_allow: {page3_next_allow}</p>
<p>Data page4_next_allow: {page4_next_allow}</p>
<p>Data page5_next_allow: {page5_next_allow}</p>
-->


<button class='button_style' on:click={back_state}> <img height=40 src="./img/back.png"> </button>


{#if page3_next_allow==false && cur_state == 2}	
	<button class='button_style'> <img height=40 src="./img/next_off.png"> </button>
{/if}

{#if page4_next_allow==false && cur_state == 3}	
	<button class='button_style'> <img height=40 src="./img/next_off.png"> </button>
{/if}

{#if page5_next_allow==false && cur_state == 4}	
	<button class='button_style'> <img height=40 src="./img/next_off.png"> </button>
{/if}


{#if page3_next_allow==true && cur_state == 2}	
	<button class='button_style' on:click={next_state}> <img height=40 src="./img/next.png"> </button>
{/if}

{#if page4_next_allow==true && cur_state == 3}	
	<button class='button_style' on:click={next_state}> <img height=40 src="./img/next.png"> </button>
{/if}

{#if page5_next_allow==true && cur_state == 4}	
	<button class='button_style' on:click={next_state}> <img height=40 src="./img/next.png"> </button>
{/if}



<style>
	.button_style {
		padding: 0;
		border: none;
		background: none;
	}
</style>