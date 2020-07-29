<script>
	import Idea from './idea.svelte'
	import { onMount } from 'svelte'

	import axios from "axios"

	let ideas = []

	const api = axios.create({
		timeout: 4000,
		crossdomain: true,
	})

	async function getIdeas() {
		let res = []

		await api.get('http://localhost:8000/ideas/', {
			page_count: 10,
			pages_skip: 0,
			pages: 1
		})
		.then((response) => {
			response.data.forEach((idea) => {
				res.push(idea.fields)
			})
		})
		.catch((error) => {
			console.log(error)
		})

		return res
	}

	onMount(async () => {
		ideas = await getIdeas()
	})

</script>


{#each ideas as idea}

	<Idea {...idea}/>

{/each}