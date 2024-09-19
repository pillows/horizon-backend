
# Horizon Assignment Backend

## Prerequisites
- Docker
- Docker Compose

## Setup Instructions

1. **Clone the repository:**
    ```sh
    git clone http://github.com/pillows/horizon-backend.git
    cd horizon-backend
    ```

2. **Fill in the `.env` file:**
    - Create a `.env` file in the root directory of the project.
    - Add the necessary environment variables as required by your application. Refer to the `.env.example` file.

3. **Start the Docker Compose services:**
    ```sh
    docker-compose up --build
    ```

4. **Access the application:**
    - Once the services are up and running, you can access the application at `http://localhost:<port>` (replace `<port>` with the appropriate port number specified in your Docker Compose file).

## Additional Commands

- **Stop the services:**
    ```sh
    docker-compose down
    ```

- **Rebuild the services:**
    ```sh
    docker-compose up --build
    ```

- **View logs:**
    ```sh
    docker-compose logs -f
    ```

## Troubleshooting

- Ensure Docker and Docker Compose are installed and running on your machine.
- Verify that the `.env` file contains all the required environment variables.
- Check the logs for any errors using the `docker-compose logs -f` command.