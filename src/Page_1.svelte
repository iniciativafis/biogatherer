<script>
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();

    let cur_state = 0;

    function next_state (){
        cur_state += 1;
        dispatch('increment', cur_state);
    }

	//let trigger = false;
	//function reset_values (){
	//	console.log('MUDAR AQUI')
	//	let trigger = true;		
	//}

	function button_action (){
	//	reset_values ();
		next_state();
	}

</script>

<spacing>-</spacing>
<br>

<img  height=75 src="./img/logo_main.png">

<br>
<spacing>-</spacing>
<br>

<p>Faça agora um novo registro!</p>
<spacing>-</spacing>
<p1>Registre uma nova sequência de áudios!</p1>
<br>
<p1>Basta seguir o passo a passo!</p1>
<br>
<spacing>-</spacing>
<br>
<p2>Nova tosse</p2>
<br>

<spacing>-</spacing>

<button class='button_style' on:click={button_action}> <img height=80 src="./img/add.png"> </button>

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

	p2 {
        font-size: 25px;
		text-align: center;
		font-weight: 800;
		/*padding: 1em;*/
		max-width: 240px;
		margin: 0 auto;
	}

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