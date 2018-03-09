<script type="text/javascript">
    function ReactHabitatBootstrap() {
        this.app = ReactHabitat.createBootstrapper({
            container: [
                {% for each in components %}
                {register: '{{ each }}', for: {{ each }} },
                {% endfor %}
            ]
        });

        window.updateHabitat = this.app.update.bind(this.app);
    };

    new ReactHabitatBootstrap();
</script>