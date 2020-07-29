<script>
	import Idea from './idea.svelte'

	let ideas = [
			{
			id:"ELOE2",
			title:"Hand-shaking machine",
			pitch:"A mechanical arm on times square that you can shake hands with and there is another hand on Tiamen square so you can shake hands with a stranger on the other side of the globe!",
		},
		{
			id:"LJ3TV",
			title:"Über but for washing clothes",
			pitch:"I need very talented programmer for free build an app where people can have can order might wash clothes",
		},
		{
			id:"KTV75Y",
			title:"Mint-flavoured soda",
			pitch:"Should have a picture of a watermelon and a palm tree on the front. Comes in extra tall cans.",
		}
	]
</script>

	<main>
	<section class="add-idea">
	<!-- TODO: Add-idea component -->
	</section>


	<section class="ideas">
		{#each ideas as idea}

			<Idea {...idea}/>

		{/each}
	</section>
	</main>


<style>
</style>