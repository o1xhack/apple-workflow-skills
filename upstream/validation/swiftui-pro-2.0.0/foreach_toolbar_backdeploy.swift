import SwiftUI
struct Sample: View { var body: some View {
 Text("A").toolbar { ForEach(0..<3) { i in ToolbarItem { Button("\(i)") {} } } }
} }
