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
                string destiny = (string)data["destiny"];

                JArray positionArray = (JArray)data["position"];
                float x = (float)positionArray[0];
                float y = 1.25f;
                float z = (float)positionArray[1];

                if(type == "Car")
                {
                    int speed = (int)data["speed"];
                    float fuel = (int)data["fuel"];
                    Debug.Log($"Coche recibido: ID={id}, Estado={status}, Posición=({x}, {z}), Velocidad={speed}, Combustible={fuel}, Destino={destiny}");
                }
                else if (type == "Person")
                {
                    Debug.Log($"Persona recibida: ID={id}, Estado={status}, Posición=({x}, {z}), Destino={destiny}");
                }


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
