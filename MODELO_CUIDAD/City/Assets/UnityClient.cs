using System;
using System.Collections;
using System.Collections.Generic;
using WebSocketSharp;
using Newtonsoft.Json.Linq;
using UnityEngine;

public class UnityClient : MonoBehaviour
{
    public string url = "ws://localhost:8765";
    private WebSocket ws;

    void Start()
    {
        ws = new WebSocket(url);
        
    
        ws.OnMessage += (sender, e) =>
        {
            try
            {
                JObject data = JObject.Parse(e.Data);

                
                int id = (int)data["id"];
                string type = (string)data["type"];  
                string status = (string)data["status"];
                int x = (int)data["x"];
                int y = (int)data["y"];
                int z = (int)data["z"];

                Debug.Log($"Mensaje recibido: ID={id}, Tipo={type}, Estado={status}, Posición=({x}, {y}, {z})");
            }
            catch (Exception ex)
            {
                Debug.LogError("Error al procesar el mensaje WebSocket: " + ex.Message);
            }
        };

    
        ws.Connect();
    }

    void OnApplicationQuit()
    {
        if (ws != null)
        {
            ws.Close();
            Debug.Log("Conexión WebSocket cerrada.");
        }
    }
}
