<script>
	import Idea from './idea.svelte'
	import { onMount } from 'svelte'

	import axios from "axios"

	let ideas = []

	const api = axios.create({
		timeout: 4000,
		crossdomain: true,
	})

	onMount(async () => {
		api.get('http://localhost:8000/ideas/', {
			page_count: 10,
			pages_skip: 0,
			pages: 1
		})
		.then((response) => {
			response.data.forEach((idea) => {
				ideas.push(idea)
			})

			alert(JSON.stringify(ideas))
		})
		.catch((error) => {
			console.log(error)
		})
	})

</script>

<main>
	
</main>
