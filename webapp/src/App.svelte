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
				let id = idea.pk
				let new_idea = idea.fields

				new_idea["id"] = id

				res.push(new_idea)
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

<main>
	<section class="add-idea">
	TODO: Add idea component
	</section>


	<section class="ideas">
		{#each ideas as idea}

			<Idea {...idea}/>

		{/each}
	</section>
</main>


<style>

	main {
		display: flex;
	}
	section {
		flex-grow: 1;
		flex-shrink: 1;
		width: 50%;
	}

	@media only screen and (max-width: 960px) {
		main {
			display: inherit;
		}

		section {
			width: unset;
		}
	}

</style>