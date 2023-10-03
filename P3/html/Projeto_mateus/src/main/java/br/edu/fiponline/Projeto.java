package br.edu.fiponline;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.PrintWriter;

@WebServlet("/projeto")
public class Projeto extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) {
        try {
            PrintWriter out = response.getWriter();
            out.println("<!DOCTYPE html>");
            out.println("<html>");
            out.println("<body>");
            out.println("<h1>Adrielly Vitória</h1>");
            out.println("</body>");
            out.println("</html>");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
