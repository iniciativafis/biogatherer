<script>
	import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();

	let cur_state = 6;

	function restart_app (){
    //    cur_state = 0;
    //    dispatch('increment', cur_state);
		location.reload()
    }

</script>

<p> <img  height=25 src="./img/p_5.png"> Salvo</p>
<spacing>-</spacing>
<br>
<p1>Registro feito com sucesso!</p1>
<br>
<spacing>-</spacing>
<br>
<p2>Clique na imagem abaixo para iniciar um novo registro</p2>
<br>
<spacing>-</spacing>
<br>

<button class='button_style' on:click={restart_app}> <img width=70 height=70 src="./img/ok.png"> </button>
<br>
<p3>Tudo certo!</p3>

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
		font-weight: 600;
	}

	p2 {		
		/*font-size: 2em;*/
		font-size: 15.5px;
		font-weight: 400;
	}

	p3 {
		color: #71e7ac;		
        font-size: 20px;
		text-align: center;
		font-weight: 500;
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