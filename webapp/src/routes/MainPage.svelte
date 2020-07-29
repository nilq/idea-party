<script>
	import Ideas from "../components/Ideas.svelte"
	import AddIdea from "../components/AddIdea.svelte"

	let ideasComponent

	function handleIdeaAdded() {
		ideasComponent.getIdeas()
	}
</script>


<main>

	<section class="add-idea">
		<AddIdea on:ideaAdded={handleIdeaAdded} />
	</section>


	<section class="ideas">
		<Ideas bind:this={ideasComponent}/>
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