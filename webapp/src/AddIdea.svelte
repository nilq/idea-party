<script>
    import { writable } from 'svelte/store';

	import axios from "axios"

    const idea = writable({
        title: "",
        pitch: "",
    })

    const api = axios.create({
		timeout: 4000,
		crossdomain: true,
    })

    async function shareIdea() {
        if ($idea.title.length > 0 && $idea.pitch.length > 0) {
            api.post('http://localhost:8000/ideas/idea/', {
                ...$idea
            })
            .catch((error) => {
                console.log(error)
            })

            $idea.title = ""
            $idea.pitch = ""
        }
    }

</script>

<style>
    .root {
        width: 90%;
        margin-left: 5%;
    }

    .content {
        display: grid;
    }

    .share-button {
        width: 100%;
    }
</style>

<div class="root">
    <form class="content">
        <input type="text" placeholder="Title" bind:value="{$idea.title}"/>
        <textarea bind:value="{$idea.pitch}"/>
    </form>

    <button class="share-button" on:click={shareIdea}>Let's go</button>
</div>