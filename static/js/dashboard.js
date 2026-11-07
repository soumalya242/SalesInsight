
async function loadKPIs() {
    try {
        const response = await fetch("/api/kpis");

        if (!response.ok) {
            throw new Error("Failed to load KPI data");
        }

        const data = await response.json();

        const currencyFormatter = new Intl.NumberFormat("en-IN", {
            style: "currency",
            currency: "INR",
            maximumFractionDigits: 2
        });

        const numberFormatter = new Intl.NumberFormat("en-IN");

        document.getElementById("total-sales").textContent =
            currencyFormatter.format(data.total_sales);

        document.getElementById("total-profit").textContent =
            currencyFormatter.format(data.total_profit);

        document.getElementById("total-orders").textContent =
            numberFormatter.format(data.total_orders);

        document.getElementById("total-quantity").textContent =
            numberFormatter.format(data.total_quantity);

        document.getElementById("average-order-value").textContent =
            currencyFormatter.format(data.average_order_value);

    } catch (error) {
        console.error("KPI loading error:", error);
    }
}



async function loadMonthlySales() {
    try {
        const response = await fetch("/api/monthly-sales");
        
        if (!response.ok) {
            throw new Error("Failed to load monthly sales");
        }
        
        const data = await response.json();
        
        // Extract month labels
        const months = data.map(item => item.month);
        
        // Extract sales values
        const sales = data.map(item => item.sales);
        
        // Create chart
        const trace = {
            x: months,
            y: sales,
            type: "scatter",
            mode: "lines",
            name: "Monthly Sales",
            line: {
                color: "#5145F5",
                width: 3,
                shape: "spline"
            },
            fill: "tozeroy",
            fillcolor: "rgba(81, 69, 245, 0.08)"
        };

        const layout = {
            autosize: true,
            margin: {
                t: 20,
                r: 20,
                b: 60,
                l: 70
            },
            xaxis: {
                title: "Month",
                tickangle: -45,
                showgrid: false
            },
            yaxis: {
                title: "Sales",
                gridcolor: "#E2E8F0",
                zeroline: false
            },
            paper_bgcolor: "white",
            plot_bgcolor: "white",
            font: {
                family: "Arial",
                color: "#64748B"
            }
        };
        
        Plotly.newPlot(
            "monthly-sales-chart",
            [trace],
            layout,
            {
                responsive: true,
                displayModeBar: false
            }
        );
        
    } catch (error) {
        console.error("Monthly sales chart error:", error);
    }
}


async function loadCategorySales() {
    try {
        const response = await fetch("/api/category-sales");

        if (!response.ok) {
            throw new Error("Failed to load category sales");
        }

        const data = await response.json();

        const categories = data.map(item => item.category);
        const sales = data.map(item => item.sales);

        const trace = {
            x: categories,
            y: sales,
            type: "bar",
            marker: {
                color: ["#5145F5", "#818CF8", "#A5B4FC"],
                borderRadius: 8
            }
        };

        const layout = {
            autosize: true,
            margin: {
                t: 20,
                r: 20,
                b: 60,
                l: 80
            },
            xaxis: {
                title: "Category"
            },
            yaxis: {
                title: "Sales",
                gridcolor: "#E2E8F0"
            },
            paper_bgcolor: "white",
            plot_bgcolor: "white"
        };

        Plotly.newPlot(
            "category-sales-chart",
            [trace],
            layout,
            {
                responsive: true,
                displayModeBar: false
            }
        );

    } catch (error) {
        console.error("Category chart error:", error);
    }
}


async function loadRegionAnalysis() {
    try {
        const response = await fetch("/api/region-analysis");

        if (!response.ok) {
            throw new Error("Failed to load regional data");
        }

        const data = await response.json();

        const regions = data.map(item => item.region);
        const sales = data.map(item => item.sales);
        const profit = data.map(item => item.profit);

        const salesTrace = {
            x: regions,
            y: sales,
            type: "bar",
            name: "Sales",
            marker: {
                color: "#5145F5"
            }
        };

        const profitTrace = {
            x: regions,
            y: profit,
            type: "bar",
            name: "Profit",
            marker: {
                color: "#A5B4FC"
            }
        };

        const layout = {
            barmode: "group",
            autosize: true,
            margin: {
                t: 20,
                r: 20,
                b: 50,
                l: 80
            },
            xaxis: {
                title: "Region"
            },
            yaxis: {
                title: "Amount",
                gridcolor: "#E2E8F0"
            },
            legend: {
                orientation: "h",
                y: 1.12
            },
            paper_bgcolor: "white",
            plot_bgcolor: "white"
        };

        Plotly.newPlot(
            "region-chart",
            [salesTrace, profitTrace],
            layout,
            {
                responsive: true,
                displayModeBar: false
            }
        );

    } catch (error) {
        console.error("Regional chart error:", error);
    }
}



