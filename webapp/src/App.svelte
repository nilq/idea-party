<script>
	import Ideas from "./Ideas.svelte"
	import AddIdea from "./AddIdea.svelte"
</script>

<main>
	<section class="add-idea">
		<AddIdea />
	</section>


	<section class="ideas">
		<Ideas/>
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