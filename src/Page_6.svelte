<script>
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();

    let cur_state = 5;

    let formPreenchido = false; // Variável para controlar se o formulário está preenchido

    let jsonData; // Variável global para armazenar os dados do formulário

    function next_state (){
        cur_state += 1;
        dispatch('increment', cur_state);
    }	

    function back_state (){
        cur_state -= 1;
        dispatch('increment', cur_state);
    }    

    function isFormPreenchido() {
        // Verificar se todos os campos do formulário estão preenchidos
        const fumante = document.querySelector('input[name="fumante"]:checked');
        const idade = document.querySelector('input[name="idade"]');
        const sexo = document.querySelector('input[name="sexo"]:checked');
        const pneumo = document.querySelector('input[name="pneumo"]:checked');
        const doenc_resp = document.querySelector('input[name="doenc_resp"]:checked');
        const covid = document.querySelector('input[name="covid"]:checked');

        return fumante && idade.value && sexo && pneumo && doenc_resp && covid;
    }

    function salvarFormulario() {
        const data = date;
        const fumante = document.querySelector('input[name="fumante"]:checked').value;
        const idade = document.querySelector('input[name="idade"]').value;
        const sexo = document.querySelector('input[name="sexo"]:checked').value;
        const pneumo = document.querySelector('input[name="pneumo"]:checked').value;
        const doenc_resp = document.querySelector('input[name="doenc_resp"]:checked').value;
        const covid = document.querySelector('input[name="covid"]:checked').value;
        const feedback = document.querySelector('textarea[name="feedback"]').value;

        const sintomasSelecionados = Array.from(document.querySelectorAll('input[name="sint"]:checked')).map((checkbox) => checkbox.value);

        const formulario = {
            data,
            fumante,
            idade,
            sexo,
            pneumo,
            doenc_resp,
            covid,
            feedback,

            sint: sintomasSelecionados
        };

        jsonData = JSON.stringify(formulario, null, 2);

        // Salvar o arquivo JSON
        //const link = document.createElement('a');        

        //link.href = 'data:text/json;charset=utf-8,' + encodeURIComponent(jsonData);
        //link.download = 'formulario_{}.json'.format(date);
        //link.click();
    }

    // Função para validar se a idade é um número inteiro
    function validarIdade() {
        const inputIdade = document.querySelector('input[name="idade"]');
        const idade = parseInt(inputIdade.value);

        if (isNaN(idade) || idade % 1 !== 0) {
        inputIdade.setCustomValidity('Informe um número inteiro para a idade.');
        } else {
        inputIdade.setCustomValidity('');
        }
    }

    function back_work (){        
        console.log(jsonData)
        //fetch('http://localhost:5000/upload-info', {
        fetch('https://biogatherer-x4fs6sryfq-rj.a.run.app/upload-info', {
            mode: 'cors',
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: jsonData,})
        .then((response) => response.json())
        //;
        .then((data) => {
            console.log('OK!')
            console.log(data)
        })
        .catch((error) => {
            console.log('ERRO!')
            console.log(error)
        });
    }

    function button_action() {
        next_state();
        salvarFormulario();
        back_work();
    }

    export let date;

    String.prototype.format = function () {
        var i = 0, args = arguments;
        return this.replace(/{}/g, function () {
            return typeof args[i] != 'undefined' ? args[i++] : '';
        });
    };

</script>


<p> <img style="vertical-align:middle" height=25 src="./img/p_4.png"> Anamnese</p>

<spacing>-</spacing>
<br>

<p2>Estamos quase lá, responda algumas informações sobre o paciente, por favor!</p2>

<br>

<form on:input="{() => formPreenchido = isFormPreenchido()}">


    <spacing>-</spacing>
    <br>
	<div>
		<p1> Qual o sexo biológico do paciente?<r>*</r> </p1>
        <label>Masculino<input type="radio"
                          name="sexo"
                          value="masc" />
        </label>
        <label>Feminino<input type="radio"
                            name="sexo"
                            value="fem" />
        </label>
	</div>

    <spacing>-</spacing>
    <br>
    <div>
		<p1> O paciente está com pneumonia?<r>*</r> </p1>
        <label>Sim<input type="radio"
                          name="pneumo"
                          value="sim_pneumo" />
        </label>
        <label>Incerto<input type="radio"
            name="pneumo"
            value="incerto_pneumo" />
        </label>
        <label>Não<input type="radio"
                            name="pneumo"
                            value="nao_pneumo" />
        </label>
	</div>

    <spacing>-</spacing>
    <br>
    <div>
		<p1> O paciente já foi diagnosticado com COVID-19?<r>*</r> </p1>
        <label>Sim<input type="radio"
                          name="covid"
                          value="sim_covid" />
        </label>        
        <label>Não<input type="radio"
                            name="covid"
                            value="nao_covid" />
        </label>
	</div>

    <spacing>-</spacing>
    <br>
    <div>
		<p1> O paciente está com alguma outra doença respiratória?<r>*</r> </p1>
        <label>Sim<input type="radio"
                          name="doenc_resp"
                          value="sim_doenc_resp" />
        </label>
        <label>Não<input type="radio"
                            name="doenc_resp"
                            value="nao_doenc_resp" />
        </label>
	</div>

    <spacing>-</spacing>
    <br>
	<div>
		<p1> O paciente fuma?<r>*</r> </p1>		
        <label>Sim<input type="radio"
                          name="fumante"
                          value="sim_fuma" />
        </label>
        <label>Não<input type="radio"
                            name="fumante"
                            value="nao_fuma" />
        </label>
	</div>

    <spacing>-</spacing>
    <br>
	<div>
		<label for='idade'> <p1> Qual é a idade do paciente?<r>*</r> </p1> </label>
		<input name='idade' type="number" inputmode="numeric" pattern="[0-9]{3}" title="Insira a idade. Use apenas números. (ex: 18)" on:input={validarIdade} min="1" max="130" step="1"/>
	</div>

    <spacing>-</spacing>
    <br>
    <div>
        <p1> O paciente possui algum dos sintomas a seguir? </p1>
        <label> Tosse seca ou secretiva <input type="checkbox"
            name="sint" id="s1" value="tosse_seca_secre" />
        </label>
        <label> Febre acima dos 38ºC <input type="checkbox"
            name="sint" id="s2" value="febre_38" />
        </label>
        <label> Calafrios <input type="checkbox"
            name="sint" id="s3" value="calafrio" />
        </label>
        <label> Dor torácica <input type="checkbox"
            name="sint" id="s4" value="dor_torax" />
        </label>
        <label> Dispneia (falta de ar) <input type="checkbox"
            name="sint" id="s5" value="dispneia" />
        </label>
    </div>


    <spacing>-</spacing>
    <br>
	<div>
		<label for='feedback'> <p1> Sugestões e comentários: </p1> </label>
        <br>
		<textarea name='feedback' cols="35" rows="5" maxlength="225" style="resize: none;" />
        <spacing>-</spacing>
        <br>
	</div>

</form>

<spacing>-</spacing>
<br>

<button class='button_style' on:click={back_state}> <img height=40 src="./img/back.png"> </button>

{#if formPreenchido}    
    <button class='button_style' on:click={button_action}> <img height=40 src="./img/next.png"> </button>
{:else}
    <button class='button_style'> <img height=40 src="./img/next_off.png"> </button>
{/if}

<br>
<spacing>-</spacing>
<br>

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

    .button_style {
		padding: 0;
		border: none;
		background: none;
	}

    spacing {
		color: #ffffff;		
		font-size: 1em;
	}

    r {
        color: red;
    }
</style>