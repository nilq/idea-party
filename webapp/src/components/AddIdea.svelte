<script>
    import { writable } from 'svelte/store'
	import { createEventDispatcher } from 'svelte'

    import axios from "axios"
    
    const dispatch = createEventDispatcher()

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
            api.post('http://0.0.0.0:8000/ideas/idea/', {
                ...$idea
            })
            .then(success => {
                dispatch('ideaAdded', { idea: $idea })

                $idea.title = ""
                $idea.pitch = ""
            })
            .catch((error) => {
                console.log(error)
            })
        }
    }

</script>

<style>
    .root {
        position: fixed;
        width: 30%;

        background-color: #FFF;
        border: 2px solid #DEDEDE;

        box-shadow: 5px 5px 2px #DEDEDE;

        padding: 30px;
        margin-left: 10%;
        margin-top: 10%;
    }

    @media only screen and (max-width: 960px) {
        .root {
            position: static;
            width: 70%;
        }
    }

    .content {
        display: grid;
    }

    textarea {
        resize: vertical;
    }

    .share-button {
        width: 100%;
        cursor: pointer;
        border-radius: 0px;
    }

    .input {
        border: 2px solid #DEDEDE;
        border-radius: 0px;
        font-family: Fira;

        width: 100%;
    }

    .huge {
        height: 50px;
    }

    .pitch {
        height: 150px;
    }

    h3 {
        margin-bottom: 25px;
    }

    .label {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 7px;

        color: #555;
    }

    .red {
        color: red;
    }
</style>

<div class="outer">
    <div class="root">
        <h3>Empty your brain</h3>

        <form class="content">
            <h5 class="label">Name the idea <span class="red">*</span></h5>
            <input type="text" bind:value="{$idea.title}" class="input huge" placeholder="The title."/>
            <h5 class="label">Non-optional pitch <span class="red">*</span></h5>
            <textarea bind:value="{$idea.pitch}" class="input pitch" placeholder="Maybe some details here."/>
        </form>

        <br>

        <button class="share-button btn btn-hg btn-primary" on:click={shareIdea}>Let's go</button>
    </div>
</div>