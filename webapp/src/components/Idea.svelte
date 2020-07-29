<script>
    export let title
    export let pitch
    export let id
    export let parent
    export let votes
    export let creation_date
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

    <p>
        {pitch}
    </p>
</article>

<style>
    article {
        background: #FFF;
        box-shadow: 3px 3px 2px #DEDEDE;

        padding: 15px;
        margin: 10px;

        margin-bottom: 15px;
    }

    span.heading {
        display: flex;
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