<script>
    export let title
    export let pitch
    export let id

    function handleClick() {
        alert("Not implemented!")
    }
</script>

<article class="root" on:click={handleClick}>

    <span class="heading">
        <h1>
            {title}
        </h1> 

        <span class="id">
            {id}
        </span>
    </span>

    <p>
        {pitch}
    </p>
</article>

<style>
    article {
        border: 1px solid lightgray;
        box-shadow: 1px 1px 4px 1px lightblue;
        border-radius: 8px;
        padding: 15px;
        margin: 10px;
        cursor: pointer;
        transition: 0.2s ease-in;
    }

    article:hover {
        box-shadow: 1px 1px 4px 4px lightblue;
    }

    span.heading {
        display: flex;
    }

    h1 {
        flex-grow: 1;
        margin-top: 0;
        margin-bottom: 0;
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