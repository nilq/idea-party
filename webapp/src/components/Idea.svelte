<script>
    export let title
    export let pitch
    export let id
    export let parent
    export let votes
    export let creation_date


    import axios from "axios"
    import Cookies from 'js-cookie'

    let already_dooted = Cookies.get(id) === 'yes.'

    const api = axios.create({
		timeout: 4000,
		crossdomain: true,
    })

    async function upWeGo() {
        api.post('http://0.0.0.0:8000/ideas/idea/vote/', {
            id: id,
            up: Cookies.get(id) !== 'yes.'
        })
        .then(success => {
            if (Cookies.get(id) === 'yes.') {
                votes -= 1
                Cookies.remove(id)
                already_dooted = false
            } else {
                votes += 1
                already_dooted = true
                Cookies.set(id, 'yes.')
            }
        })
        .catch((error) => {
            console.log(error)
        })
    }
</script>

<article class="root">
    <span class="heading">
        <h5>
            {title}
        </h5>

        <span class="id">
            {id}
        </span>
    </span>

    <p class="pitch">
        {pitch}
    </p>

    <br>

    <div style="display: flex;" class="votes">
        <button class="{already_dooted ? 'btn btn-lg the-votes' : 'btn btn-lg the-votes' }" style="width: 60px;">{votes}</button>
        <button class="{already_dooted ? 'btn btn-lg btn-default up-button' : 'btn btn-lg btn-primary up-button' }" on:click={upWeGo}>{already_dooted ? 'Liked' : 'Like'}</button>
    </div>
</article>

<style>

    button {
        border-radius: 0px;
    }


    .votes {
        margin-bottom: -10px;
    }

    .the-votes {
        background-color: #EEE;
        border: 1px solid #EEE;

        transition: background-color 0.5s;

        text-align: center;

        width: 50px;
    }

    .the-votes:hover {
        width: 50px;

        background-color: #EEE;
        border: 1px solid #EEE;
    }

    .up-button {
        cursor: pointer;
    }

    article {
        background: #FFF;
        box-shadow: 3px 3px 2px #DEDEDE;
        border: 2px solid #DEDEDE;

        padding: 25px;
        margin: 10px;

        margin-bottom: 15px;
    }

    span.heading {
        display: flex;
        margin-bottom: 5px;
    }

    .pitch {
        white-space: pre-line;
    }

    h5 {
        flex-grow: 1;
        margin-top: 0;
        margin-bottom: 0;
        font-size: 18px;
    }

    span.id {
        font-family: 'Courier New', Courier, monospace;
        color: gray;
    }
    span.id:before {
        content: "§";
        color: red;
    }

    p {
        margin-top: 0;
        margin-bottom: 0;
    }
</style>