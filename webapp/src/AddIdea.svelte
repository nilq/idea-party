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
        border: 1px solid lightgray;
        box-shadow: 1px 1px 4px 1px lightblue;
        border-radius: 8px;
        padding: 15px;
        margin: 10px;
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