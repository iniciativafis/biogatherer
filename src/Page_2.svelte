<script>
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();

    let cur_state = 1;

    function next_state (){
        cur_state += 1;
        dispatch('increment', cur_state);
    }
</script>


<p>Instruções</p>

<spacing>-</spacing>
<br>

<p1>
	<img style="vertical-align:middle" height=25 src="./img/item_1.png"> Ao fim da consulta, certifique-se que o ambiente está silencioso. Dê as devidas instruções ao paciente sobre o procedimento que irá realizar.
	<br>
	<img  height=200 src="./img/fig_1.png">
	<spacing>-</spacing>
	<br>
	<img style="vertical-align:middle" height=25 src="./img/item_2.png"> Nas etapas de gravação, mantenha o aparelho à uma distância de 30-60cm do paciente. Não obstrua ou cubra o aparelho.
	<br>	
	<img  height=200 src="./img/fig_2.png">
	<spacing>-</spacing>
	<br>
	<img style="vertical-align:middle" height=25 src="./img/item_3.png"> Toque no botão gravar e solicite que o paciente realize a tarefa: tossir, sustentar vogal e falar frase. Quando terminar, toque no botão de parada.
	<br>
	<img  height=200 src="./img/fig_3.png">
	<spacing>-</spacing>
	<br>
	<img style="vertical-align:middle" height=25 src="./img/item_4.png"> Preencha o formulário de anamnese com atenção.
	<br>
	<img  height=200 src="./img/fig_4.png">
	<spacing>-</spacing>
	<br>
	<img style="vertical-align:middle" height=25 src="./img/item_5.png"> Confirme e estará pronto!!
</p1>
<br>

<h1>-</h1>

<button class='button_style' on:click={next_state}> <img height=40 src="./img/next.png"> </button>

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

	.button_style {
		padding: 0;
		border: none;
		background: none;

		position: sticky;
      	bottom: 70px;		

  
	}

	h1 {
		color: #ffffff;		
		font-size: 1em;
	}

	spacing {
		color: #ffffff;		
		font-size: 1em;
	}
</style>