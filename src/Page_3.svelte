<script>	
	import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();

	let cur_state = 2;

	function next_state (){
        cur_state += 1;
        dispatch('increment', cur_state);
    }	

	function back_state (){
        cur_state -= 1;
        dispatch('increment', cur_state);
    }

	export let page3_next_allow;
</script>


<p> <img  height=25 src="./img/p_1.png"> Tosse </p>
<p1>Grave agora uma sequência de tosse:</p1>
<br>
<button type="button"> Preferencialmente uma sequência de três tosses seguidas. </button> 


<style>
	p {
        font-size: 25px;
		text-align: center;
		font-weight: 800;
		/*padding: 1em;*/
		max-width: 240px;
		margin: 0 auto;
	}

	p1 {		
		/*font-size: 2em;*/
		font-size: 15.5px;
		font-weight: 400;
	}	
</style>