<script>
	import Header from './Header.svelte';
	import Footer from './Footer.svelte';

	import Next_Back from "./Next_Back.svelte";
	import Recorder from "./Recorder.svelte";

	import Page_1 from './Page_1.svelte';
	import Page_2 from './Page_2.svelte';
	import Page_3 from './Page_3.svelte';
	import Page_4 from './Page_4.svelte';
	import Page_5 from './Page_5.svelte';
	import Page_6 from './Page_6.svelte';
	import Page_7 from './Page_7.svelte';

	let state_ctrl = 0;
	function handleIncrement(event) {
    	state_ctrl = event.detail;
  	}

	let page3_next_allow = false;
	function handleStateChange_page3(newValue_p3) {
    	page3_next_allow = newValue_p3;
  	}

	let page4_next_allow = false;
	function handleStateChange_page4(newValue_p4) {
    	page4_next_allow = newValue_p4;
  	}

	let page5_next_allow = false;
	function handleStateChange_page5(newValue_p5) {
    	page5_next_allow = newValue_p5;
  	}

	let date = new Date().toJSON().slice(0 , 19).replace(/-/g,'').replace(/:/g,'').replace(/T/g,'_');	

</script>

<Header/>

<main>
	
	<h1>-</h1>
	

	<!--
	<p>Página: {state_ctrl+1}</p>
	<p>teste: {page3_next_allow}</p>
	<p>Data: {date}</p>
	-->

	{#if state_ctrl==0}		
		<Page_1 bind:cur_state={state_ctrl} on:increment={handleIncrement}/>
	{/if}
	{#if state_ctrl==1}		
		<Page_2 bind:counter={state_ctrl} on:increment={handleIncrement}/>
	{/if}
	{#if state_ctrl==2}
		<Page_3 {page3_next_allow} bind:counter={state_ctrl} on:increment={handleIncrement}/>		
		<Recorder {state_ctrl} {date} bind:page3_next_allow={page3_next_allow} on:change={handleStateChange_page3}/>		
		<Next_Back {state_ctrl} {page3_next_allow} {page4_next_allow} {page5_next_allow} bind:counter={state_ctrl} on:increment={handleIncrement}/>
		<br>
		<img height=15 src="./img/ellipse_full.png">
		<img height=15 src="./img/ellipse_empty.png">
		<img height=15 src="./img/ellipse_empty.png">
		<img height=15 src="./img/ellipse_empty.png">
		<img height=15 src="./img/ellipse_empty.png">
	{/if}
	{#if state_ctrl==3}
		<Page_4 {page4_next_allow} bind:counter={state_ctrl} on:increment={handleIncrement}/>
		<Recorder {state_ctrl} {date} bind:page4_next_allow={page4_next_allow} on:change={handleStateChange_page4}/>
		<Next_Back {state_ctrl} {page3_next_allow} {page4_next_allow} {page5_next_allow} bind:counter={state_ctrl} on:increment={handleIncrement}/>
		<br>
		<img height=15 src="./img/ellipse_full.png">
		<img height=15 src="./img/ellipse_full.png">
		<img height=15 src="./img/ellipse_empty.png">
		<img height=15 src="./img/ellipse_empty.png">
		<img height=15 src="./img/ellipse_empty.png">
	{/if}
	{#if state_ctrl==4}
		<Page_5 {page5_next_allow} bind:counter={state_ctrl} on:increment={handleIncrement}/>
		<Recorder {state_ctrl} {date} bind:page5_next_allow={page5_next_allow} on:change={handleStateChange_page5}/>
		<Next_Back {state_ctrl} {page3_next_allow} {page4_next_allow} {page5_next_allow} bind:counter={state_ctrl} on:increment={handleIncrement}/>
		<br>
		<img height=15 src="./img/ellipse_full.png">
		<img height=15 src="./img/ellipse_full.png">
		<img height=15 src="./img/ellipse_full.png">
		<img height=15 src="./img/ellipse_empty.png">
		<img height=15 src="./img/ellipse_empty.png">
	{/if}
	{#if state_ctrl==5}
		<Page_6 {date} bind:counter={state_ctrl} on:increment={handleIncrement}/>
		<br>
		<img height=15 src="./img/ellipse_full.png">
		<img height=15 src="./img/ellipse_full.png">
		<img height=15 src="./img/ellipse_full.png">
		<img height=15 src="./img/ellipse_full.png">
		<img height=15 src="./img/ellipse_empty.png">
	{/if}
	{#if state_ctrl==6}
		<Page_7 bind:counter={state_ctrl} on:increment={handleIncrement}/>
	{/if}
</main>

<h1>-</h1>

<Footer/>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		/*color: #008ac0;*/
		color: #ffffff;
		text-transform: uppercase;
		font-size: 2em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}	
</style>