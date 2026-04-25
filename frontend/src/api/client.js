const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

async function request(path, options = {}) {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    headers: {
      "Content-Type": "application/json",
      ...(options.headers || {}),
    },
    ...options,
  });

  if (!response.ok) {
    const message = await response.text();
    throw new Error(message || `Request failed: ${response.status}`);
  }

  return response.json();
}

export const api = {
  baseUrl: API_BASE_URL,
  getMeals: (params = {}) => {
    const searchParams = new URLSearchParams();
    Object.entries(params).forEach(([key, value]) => {
      if (value) searchParams.set(key, value);
    });
    const suffix = searchParams.toString() ? `?${searchParams}` : "";
    return request(`/meals${suffix}`);
  },
  createMeal: (meal) =>
    request("/meals", {
      method: "POST",
      body: JSON.stringify(meal),
    }),
  createOrder: (order) =>
    request("/orders", {
      method: "POST",
      body: JSON.stringify(order),
    }),
  getOrders: () => request("/orders"),
  updateOrderStatus: (orderId, status) =>
    request(`/orders/${orderId}/status`, {
      method: "PATCH",
      body: JSON.stringify({ status }),
    }),
  getStats: () => request("/dashboard/stats"),
  getRecommendations: () => request("/ai/recommendations"),
  getPeakHours: () => request("/ai/peak-hours"),
};
