<script>
    export let title
    export let pitch
    export let id

    function handleClick() {
        alert("Not implemented!")
    }
</script>

<article class="root" on:click={handleClick}>

    <h1>
        {title}
    </h1> 

    <p>
        {pitch}
    </p>

    <span class="id">
        {id}
    </span>
</article>

<style>
    article {
        border: 1px solid lightgray;
        box-shadow: 1px 1px 4px 1px lightblue;
        border-radius: 8px;
        padding: 15px;
        margin: 10px;
        position: relative;
        cursor: pointer;
        transition: 0.2s ease-in;
    }

    article:hover {
        box-shadow: 1px 1px 4px 4px lightblue;
    }

    h1 {
        margin-top: 0;
        margin-bottom: 0;
    }

    p {
        margin-top: 0;
        margin-bottom: 0;
    }

    span.id {
        font-family: 'Courier New', Courier, monospace;
        color: gray;
        position: absolute;
        top: 15px;
        right: 15px;
    }
    span.id:before {
        content: "§";
        color: red;
    }
</style>