import SwiftUI
struct Sample: View { var body: some View {
 Text("A").toolbar { ToolbarItem { Button("Export") {} }.hidden(true) }
} }
