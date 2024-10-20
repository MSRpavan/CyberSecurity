#include <iostream>
#include <string>
#include <mysql/mysql.h> 

void login(std::string username, std::string password) {
    MYSQL *conn;
    conn = mysql_init(NULL);

    if (!mysql_real_connect(conn, "localhost", "root", "password", "testdb", 0, NULL, 0)) {
        std::cerr << "Connection Error: " << mysql_error(conn) << std::endl;
        return;
    }

    std::string query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "';";

    if (mysql_query(conn, query.c_str())) {
        std::cerr << "Query Error: " << mysql_error(conn) << std::endl;
    } else {
        MYSQL_RES *res = mysql_store_result(conn);
        if (res && mysql_num_rows(res) > 0) {
            std::cout << "Login successful!" << std::endl;
        } else {
            std::cout << "Invalid username or password." << std::endl;
        }
        mysql_free_result(res);
    }

    mysql_close(conn);
}

void registerUser(std::string username, std::string password, std::string email) {
    MYSQL *conn;
    conn = mysql_init(NULL);

    if (!mysql_real_connect(conn, "localhost", "root", "password", "testdb", 0, NULL, 0)) {
        std::cerr << "Connection Error: " << mysql_error(conn) << std::endl;
        return;
    }

    std::string query = "INSERT INTO users (username, password, email) VALUES ('" + username + "', '" + password + "', '" + email + "');";

    if (mysql_query(conn, query.c_str())) {
        std::cerr << "Query Error: " << mysql_error(conn) << std::endl;
    } else {
        std::cout << "User registered successfully!" << std::endl;
    }

    mysql_close(conn);
}

void updatePassword(std::string username, std::string newPassword) {
    MYSQL *conn;
    conn = mysql_init(NULL);

    if (!mysql_real_connect(conn, "localhost", "root", "password", "testdb", 0, NULL, 0)) {
        std::cerr << "Connection Error: " << mysql_error(conn) << std::endl;
        return;
    }

    std::string query = "UPDATE users SET password = '" + newPassword + "' WHERE username = '" + username + "';";

    if (mysql_query(conn, query.c_str())) {
        std::cerr << "Query Error: " << mysql_error(conn) << std::endl;
    } else {
        std::cout << "Password updated successfully!" << std::endl;
    }

    mysql_close(conn);
}

void deleteUser(std::string username) {
    MYSQL *conn;
    conn = mysql_init(NULL);

    if (!mysql_real_connect(conn, "localhost", "root", "password", "testdb", 0, NULL, 0)) {
        std::cerr << "Connection Error: " << mysql_error(conn) << std::endl;
        return;
    }

    std::string query = "DELETE FROM users WHERE username = '" + username + "';";

    if (mysql_query(conn, query.c_str())) {
        std::cerr << "Query Error: " << mysql_error(conn) << std::endl;
    } else {
        std::cout << "User deleted successfully!" << std::endl;
    }

    mysql_close(conn);
}

int main() {
    std::string username, password, email, newPassword;

    std::cout << "Enter username to login: ";
    std::cin >> username;
    std::cout << "Enter password: ";
    std::cin >> password;
    login(username, password);

    std::cout << "Register a new user: " << std::endl;
    std::cout << "Enter username: ";
    std::cin >> username;
    std::cout << "Enter password: ";
    std::cin >> password;
    std::cout << "Enter email: ";
    std::cin >> email;
    registerUser(username, password, email);

    std::cout << "Update password for user: " << std::endl;
    std::cout << "Enter username: ";
    std::cin >> username;
    std::cout << "Enter new password: ";
    std::cin >> newPassword;
    updatePassword(username, newPassword);

    std::cout << "Delete user: " << std::endl;
    std::cout << "Enter username to delete: ";
    std::cin >> username;
    deleteUser(username);

    return 0;
}
