<script>
	import Idea from './Idea.svelte'
	import { onMount } from 'svelte'

	import axios from "axios"

	export let ideas = []

	const api = axios.create({
		timeout: 4000,
		crossdomain: true,
	})

	export function getIdeas() {
		let res = []

		api.get('http://localhost:8000/ideas/', {
			page_count: 10,
			pages_skip: 0,
			pages: 1
		})
		.then((response) => {
			response.data.forEach((idea) => {
				let id = idea.pk
				let new_idea = idea.fields

				new_idea.id = id

				res.push(new_idea)
			})
				
			ideas = res
		})
		.catch((error) => {
			console.log(error)
		})
	}

	onMount(() => {
		getIdeas()
	})

</script>

<style>
	.root {
		margin-top: 20%;
		width: 90%;
		margin-left: 5%;
	}
</style>

<div class="root">
	{#each ideas as idea (idea.id)}

	<Idea {...idea}/>

	{/each}
</div>