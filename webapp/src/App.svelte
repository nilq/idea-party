<script>
	import { Router, Link, Route } from "svelte-routing";

	import MainPage from "./routes/MainPage.svelte"

	export let url =""
</script>

<Router url="{url}">
	<nav>
		<!-- <Link to="/">Home</Link>
		<Link to="hello">Hello</Link> -->
	</nav>
	<div>
		<Route path="/" component="{MainPage}" />
		<Route path="hello">
			, world!
		</Route>
	</div>
</Router>