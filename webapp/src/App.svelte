<script>
	import Ideas from "./Ideas.svelte"
	import AddIdea from "./AddIdea.svelte"
</script>

<main>
	<section class="add-idea">
		<div class="background"/>

		<AddIdea />
	</section>


	<section class="ideas">
		<div>
			<Ideas/>
		</div>
	</section>
</main>


<style>

	main {
		display: flex;
	}
	section {
		flex-grow: 1;
		flex-shrink: 1;
	}

	.ideas {
		width: 55%;
	}

	.background {
		z-index: -10;
		position: fixed;
		top: 0;
		left: 0;
		width: 600px;
		height: 100%;
		background-color: wheat;

		box-shadow: 5px 0px 2px #DEDEDE;
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