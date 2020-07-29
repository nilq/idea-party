<script>
    import { writable } from 'svelte/store';

    const idea = writable({
        title: "",
        pitch: "",
    })
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

    <button class="share-button">Let's go</button>
</div>